"""Flux correlation"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat
import math as m
from scipy.stats import linregress as regr 

DIST=436. #Ortiz-Leon 2017
L_sun = 3.86e26 #W  
freq = {'CN': 113490985000, 'HCN': }
c = 299792458 # m/s
k = 1.38e-23  #Boltzmann constant [J/K]

conversion_factor = {3: 22, 2: 29} #, 1.3: 35, 0.8: 45}  #[mm]:[Jy/K] from http://www.iram.fr/GENERAL/calls/s14/s14.pdf?fbclid=IwAR3_XqJE1cvy86ppQbSpXS1xAJ4F2sUjevWGDx1Nr78-rdNkUIDksY7f3n8

def read_data(filename):
	file = open(filename,'r')
	data = file.readlines()
	file.close()

	return data

def write_data(end_filename, data, slope, intercept, pearson, stderr):
	file = open(end_filename,'w')
	for SMM, CN, HCN in data:
		file.write(f'{SMM:10.5} {CN:10.5} {HCN:10.5}\n')
	file.write(f'\n slope:{slope:10.5} intercept:{intercept:10.5} stderr:{stderr:10.5} pearson:{pearson:10.5}\n')
	file.close()

def create_flux_list(data):
	fluxes = []
	for i in range(1,len(data)):
		line = data[i].split()
		previous_line = data[i-1].split()
		if line[1] == 'hcn10' and previous_line[1] == 'cn10':
			fluxes.append((line[0], float(previous_line[2]), float(line[2]), float(data[i+1].split()[2]))) # source CNflux, HCNflux, CSflux
	return fluxes

def plot_correlation(x, y, a, b, pearson):
	Y = [elem*a+b for elem in x]

	fig = plt.figure(1)
	ax = fig.add_subplot(111)
	
	ax.set_ylabel(r"$L_{\mathrm{CN}}$ [L$_\odot$]")
	ax.set_xlabel(r"$L_{\mathrm{HCN}}$ [L$_\odot$]")

	major_ticks_x = np.arange(-1, 2, 0.5)
	major_ticks_y = np.arange(-6, -5, 0.1)

	ax.set_xticks(major_ticks_x)
	ax.set_yticks(major_ticks_y)

	sources_list=['SMM8','SMM5','SMM2','SMM4','SMM12','SMM10','SMM3','SMM9','SMM6','SMM1']  #Lbol increasing
	for i in range(len(sources_list)):
		if i ==4:
			ax.text(x[i]+0.02, y[i]-0.02, 'SMM12')
		elif i == 0:
			ax.text(x[i]+0.02, y[i], 'SMM8')
		else:
			ax.text(x[i]+0.02, y[i], sources_list[i])

	ax.text(0.05, 1.05, 'Pearson coefficient = '+str(pearson) , transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom')
	
	plt.plot(x, y, 'r.', ms=4.9)
	plt.plot(x, Y, 'k-', linewidth=0.5)

	plt.savefig('CN_HCN_correlation_log', format='eps')
	plt.close()

def calculate_pearson(x, y):
	pearson = stat.pearsonr(x, y)
	print(pearson)

	return pearson[0]

def fit_linear_regression(x, y):
	slope, intercept, r_value, p_value, stderr = stat.linregress(x,y)
	print(slope, intercept, r_value, p_value, stderr)
	return slope, intercept, stderr

def sort_points(list_to_sort, other_list):
	if len(list_to_sort) != len(other_list):
		raise 
	merged_list = [(list_to_sort[i], other_list[i]) for i in range(len(list_to_sort))]
	sorted_list = sorted(merged_list, key=lambda x: x[0])
	return [elem[0] for elem in sorted_list], [elem[1] for elem in sorted_list]

def calculate_Lbol_for_molecule(fluxes, mol, JytoK):
	Lbol_source = []

	for line in fluxes:
		new_line = []
		for i in range(1,len(line)):
			flux_Jy_kms = line[i]*JytoK # 2k/lambda^2 * T_mb [Jy*km/s]
			flux_Jy_Hz = flux_Jy_kms/((c/1000.)/freq[mol])  # F [Jy*Hz] = F [Jy*km/s] / lambda[km]
			L_bol = (1e-26*flux_Jy_Hz*4.0*m.pi*(DIST*3.0857e16)**2)/L_sun 
			print(L_bol)
			new_line.append(L_bol)
		Lbol_source.append(new_line)

	return Lbol_source

def estimate_conversion_factor(freq):
	wavelength = c*1000/freq  #in mm
	mms = [elem for elem in conversion_factor.keys()]
	Jy_K = [elem for elem in conversion_factor.values()]
	a, b, r, p, stdev = regr(mms, Jy_K)
	y = a * wavelength + b

	return y


def make_log_list(old_list):
	new_list = []
	for elem in old_list:
		if elem != 0:
			new_list.append(m.log10(elem))
		else:
			new_list.append(elem)				

	return new_list

def main():
	data = read_data('SMM_fluxes') 
	fluxes = create_flux_list(data)

	JytoK_CN = estimate_conversion_factor(freq['CN'])
	JytoK_HCN = estimate_conversion_factor(freq['HCN'])
	Lbol_CN = calculate_Lbol_for_molecule(fluxes, 'CN', JytoK_CN)
	Lbol_HCN = calculate_Lbol_for_molecule(fluxes, 'HCN', JytoK_HCN)

	Lbol = [78.7, 4.1, 6.9, 4.4, 3.7, 43.1, 0.2, 10.3, 6.2, 5.7]
	Tbol = [35, 31, 35, 77, 151, 532, 15, 35, 83, 97]

	CN_list = [point[0] for point in Lbol_source]
	HCN_list = [point[1] for point in Lbol_source]
	CS_list = [point[2] for point in Lbol_source]
	Lbol, CN_list = sort_points(Lbol, CN_list)
	Lbol = make_log_list(Lbol)
	CN_list = make_log_list(CN_list)

	a, b, stderr = fit_linear_regression(Lbol, CN_list)
	pearson = calculate_pearson(Lbol, CN_list)
	plot_correlation(Lbol, CN_list, a, b, pearson)
    
	#write_data('CN_Lbol_corr.txt', fluxes, a, b, pearson, stderr)
if __name__ == '__main__':
	main()
