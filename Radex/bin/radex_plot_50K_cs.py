'''Read RADEX outputs and make a plot'''
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Helvetica']})
import matplotlib.pyplot as plt
import math as m
from matplotlib.patches import Rectangle as rec
from scipy.stats import linregress as regr 

RATIO = [-2, -1, 0, 1, 2]
TEMP = '50'
H2_dens = '1e5'


def read_data(file_name):
	radex_file = open(file_name, 'r')
	flux = radex_file.readlines()[13].split()[11]
	radex_file.close()

	return flux

def write_to_file(limits1, limits2):
	file_out = open('RADEX_N_ratio_cs.txt', 'w')
	file_out.write('Temperature   H2_density   SMM_limits    Outflow_limits \n')
	file_out.write("%s   %s  %f  %f  %f  %f \n" % (TEMP, H2_dens, limits1[0], limits1[1], limits2[0], limits2[1]))
	file_out.close()

def make_log_list(old_list):
	new_list = []
	for elem in old_list:
		if elem != 0:
			new_list.append(m.log10(elem))
		else:
			new_list.append(elem)				

	return new_list

def make_picture(ratio, fluxes, low_obs_log, high_obs_log, low_obs_log_smm, high_obs_log_smm, limits1, limits2):

	fig,ax = plt.subplots(1)
	fig.set_figheight(8)
	fig.set_figwidth(8)
	plt.plot(ratio, fluxes, 'k-')
	rect_outflow = rec((-0.5, low_obs_log), 4, high_obs_log-low_obs_log, color = 'blue', rasterized = True, alpha = 0.8)
	rect_smm = rec((-0.5, low_obs_log_smm), 4, high_obs_log_smm-low_obs_log_smm, color = 'red', rasterized = True, alpha = 0.8)
	ax.add_patch(rect_outflow)
	ax.add_patch(rect_smm)
	ax.axvline(limits1[0], linestyle = '--', color = 'green')
	ax.axvline(limits1[1], linestyle = '--', color = 'green')
	ax.axvline(limits2[0], linestyle = '--', color = 'magenta')
	ax.axvline(limits2[1], linestyle = '--', color = 'magenta')
	plt.ylabel(r'$\log(\frac{I_\mathrm{CS}}{I_\mathrm{HCN}}$)', size=20)
	plt.xlabel(r'$\log(\frac{N_\mathrm{CS}}{N_\mathrm{HCN}}$)', size=20)
	plt.ylim(-1, 0.5)
	plt.xlim(-0.5, 1)
	props = dict(boxstyle='round', facecolor='white', alpha=0.5)
	ax.text(0.1, 0.8, 'T = '+TEMP+' K \n $n_{H_2} = 10^{5}$ cm$^{-3}$', transform=ax.transAxes, fontsize=14, verticalalignment='bottom', bbox=props)

	plt.savefig('RADEX_CS_HCN_'+TEMP+'K_'+H2_dens+'.pdf')
	plt.close()

def find_ranges(low_limit, high_limit, fluxes):
	a, b, r, p, stdev = regr(RATIO, fluxes)
	x1 = (low_limit-b)/a
	x2 = (high_limit-b)/a

	return (x1, x2)


def main():
	file_name_hcn = './output_50K/hcn'+H2_dens+TEMP+'1e8.out'
	flux_hcn = float(read_data(file_name_hcn))
	fluxes_cn = []
	fluxes_cs = []
	for col_dens in ['1e6', '1e7', '1e8', '1e9', '1e10']:
		#flux_cn = float(read_data('./output_50K/cn'+H2_dens+TEMP+col_dens+'.out'))
		#fluxes_cn.append(flux_cn)
		flux_cs = float(read_data('./output_50K/cs'+H2_dens+TEMP+col_dens+'.out'))
		fluxes_cs.append(flux_cs)
	
	fluxes = [flux/flux_hcn for flux in fluxes_cs]
	fluxes_log = make_log_list(fluxes) 
	low_obs_smm = 0.49
	high_obs_smm = 0.69
	low_obs_log_smm = m.log10(low_obs_smm)
	high_obs_log_smm = m.log10(high_obs_smm)
	low_obs = 0.55
	high_obs = 0.76
	low_obs_log = m.log10(low_obs)
	high_obs_log = m.log10(high_obs)
	print(low_obs_log_smm, high_obs_log_smm, low_obs_log, high_obs_log)
	smm_ranges = 0
	smm_limits = find_ranges(low_obs_log_smm, high_obs_log_smm, fluxes_log)
	limits = find_ranges(low_obs_log, high_obs_log, fluxes_log)
	write_to_file(smm_limits, limits)
	make_picture(RATIO, fluxes_log, low_obs_log, high_obs_log, low_obs_log_smm, high_obs_log_smm, smm_limits, limits)

if __name__ == '__main__':
	main()
