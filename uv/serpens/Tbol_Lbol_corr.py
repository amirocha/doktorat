"""Flux correlation"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat
import math as m
from scipy.stats import linregress as regr 
from pylab import *

MOLECULES = ['CN', 'HCN', 'CS']
DIST=436. #Ortiz-Leon 2017
L_sun = 3.86e26 #W  
freq = [113490985000, 88631847000, 146969029000]
c = 299792458 # m/s
k = 1.38e-23  #Boltzmann constant [J/K]


rc('font', **{'family':'serif', 'serif':['Times New Roman']})
params = {'backend': 'pdf',
          #'axes.labelsize': 12,
          #'text.fontsize': 12,
          #'legend.fontsize': 12,
          #'xtick.labelsize': 7,
          #'ytick.labelsize': 7,
          # The comm. below determines whether you use LaTeX 
          # for all text in matplotlib (you probably don't want 
          # to turn this on, but may)
          'text.usetex': False,
          # four comm. below (math) determines what is used for math rendering 
          'mathtext.rm': 'serif',
          'mathtext.it': 'serif:italic',
          'mathtext.bf': 'serif:bold',
          'mathtext.fontset': 'custom',
          #'figure.figsize': fig_size,
          'axes.unicode_minus': True}
matplotlib.rcParams.update(params)

conversion_factor = {3: 22, 2: 29, 1.3: 35, 0.8: 45}  #[mm]:[Jy/K] from http://www.iram.fr/GENERAL/calls/s14/s14.pdf?fbclid=IwAR3_XqJE1cvy86ppQbSpXS1xAJ4F2sUjevWGDx1Nr78-rdNkUIDksY7f3n8

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

def create_flux_file(data, mol):
	fluxes = []
	for i in range(1,len(data)):
		line = data[i].split()
		previous_line = data[i-1].split()
		if mol == 0: #CN
			if line[1] == 'hcn10' and previous_line[1] == 'cn10':
				fluxes.append(float(previous_line[2])) # source CNflux
		if mol == 1: #HCN
			if line[1] == 'hcn10' and previous_line[1] == 'cn10':
				fluxes.append(float(line[2])) # source HCNflux
		if mol == 2: #CS
			if line[1] == 'hcn10' and previous_line[1] == 'cn10':
				fluxes.append(float(data[i+1].split()[2])) # source CSflux
	return fluxes

def plot_correlation(points, regresions, pearsons):
	fig = plt.figure(figsize = (20,20), dpi = 400)
	plt.tick_params(axis='y', which='both', right=False)
	fig.subplots_adjust(wspace=0)
	fig.subplots_adjust(hspace=0)

	ax1 = plt.subplot(3, 2, 1)
	# Set the tick labels font
	for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
	#    label.set_fontname('Arial')
   		label.set_fontsize(14)
	ax1.set_xlim([-1.0, 2.3])
	ax1.set_ylim([-6, -5.1])
	major_ticks_y = np.arange(-5.9, -5.1, 0.1)
	ax1.set_yticks(major_ticks_y)
	ax1.set_xticks([])
	plt.plot(points[0][0], points[0][1], 'k.', ms=4.9)
	Y = [elem*regresions[0][0]+regresions[0][1] for elem in points[0][0]]
	plt.plot(points[0][0], Y, 'k-', linewidth=0.5)

	ax2 = plt.subplot(3, 2, 2)
	for label in (ax2.get_xticklabels() + ax2.get_yticklabels()):
	#    label.set_fontname('Arial')
   		label.set_fontsize(14)
	ax2.set_xlim([1.0, 3.1])
	ax2.set_ylim([-6, -5.1])
	ax2.set_yticks([])
	ax2.set_xticks([])
	plt.plot(points[1][0], points[1][1], 'k.', ms=4.9)
	Y = [elem*regresions[1][0]+regresions[1][1] for elem in points[1][0]]
	plt.plot(points[1][0], Y, 'k-', linewidth=0.5)

	ax3 = plt.subplot(3, 2, 3)
	for label in (ax3.get_xticklabels() + ax3.get_yticklabels()):
	#    label.set_fontname('Arial')
   		label.set_fontsize(14)
	ax3.set_xlim([-1.0, 2.3])
	ax3.set_ylim([-6.1, -5.1])
	major_ticks_y = np.arange(-6, -5.1, 0.1)
	ax3.set_yticks(major_ticks_y)
	ax3.set_xticks([])
	plt.plot(points[2][0], points[2][1], 'k.', ms=4.9)
	Y = [elem*regresions[2][0]+regresions[2][1] for elem in points[2][0]]
	plt.plot(points[2][0], Y, 'k-', linewidth=0.5)

	ax4 = plt.subplot(3, 2, 4)
	for label in (ax4.get_xticklabels() + ax4.get_yticklabels()):
	#    label.set_fontname('Arial')
   		label.set_fontsize(14)
	ax4.set_xlim([1.0, 3.1])
	ax4.set_ylim([-6.1, -5.1])
	ax4.set_yticks([])
	ax4.set_xticks([])
	plt.plot(points[3][0], points[3][1], 'k.', ms=4.9)
	Y = [elem*regresions[3][0]+regresions[3][1] for elem in points[3][0]]
	plt.plot(points[3][0], Y, 'k-', linewidth=0.5)

	ax5 = plt.subplot(3, 2, 5)
	for label in (ax5.get_xticklabels() + ax5.get_yticklabels()):
	#    label.set_fontname('Arial')
   		label.set_fontsize(14)
	ax5.set_xlim([-1.0, 2.3])
	ax5.set_ylim([-5.8, -4.8])
	major_ticks_y = np.arange(-5.7, -4.8, 0.1)
	major_ticks_x = np.arange(-1, 2.2, 0.5)
	ax5.set_yticks(major_ticks_y)
	ax5.set_xticks(major_ticks_x)
	plt.plot(points[4][0], points[4][1], 'k.', ms=4.9)
	Y = [elem*regresions[4][0]+regresions[4][1] for elem in points[4][0]]
	plt.plot(points[4][0], Y, 'k-', linewidth=0.5)

	ax6 = plt.subplot(3, 2, 6)
	for label in (ax6.get_xticklabels() + ax6.get_yticklabels()):
	#    label.set_fontname('Arial')
   		label.set_fontsize(14)
	ax6.set_xlim([1.0, 3.1])
	ax6.set_ylim([-5.8, -4.8])
	ax6.set_yticks([])
	major_ticks_x = np.arange(1, 3.5, 0.5)
	ax6.set_xticks(major_ticks_x)
	plt.plot(points[5][0], points[5][1], 'k.', ms=4.9)
	Y = [elem*regresions[5][0]+regresions[5][1] for elem in points[5][0]]
	plt.plot(points[5][0], Y, 'k-', linewidth=0.5)
	
	ax1.set_ylabel(r"$L_{\mathrm{CN}}$ [L$_\odot$]", fontsize=18)
	ax3.set_ylabel(r"$L_{\mathrm{HCN}}$ [L$_\odot$]", fontsize=18)
	ax5.set_ylabel(r"$L_{\mathrm{CS}}$ [L$_\odot$]", fontsize=18)
	ax5.set_xlabel(r"$L_{\mathrm{bol}}$ [L$_\odot$]", fontsize=18)
	ax6.set_xlabel(r"$T_{\mathrm{bol}}$ [K]", fontsize=18)

	sources_list_Lbol = ['SMM8','SMM5','SMM2','SMM4','SMM12','SMM10','SMM3','SMM9','SMM6','SMM1']  #Lbol increasing
	sources_list_Tbol = ['SMM8','SMM2','SMM1','SMM3','SMM9','SMM4','SMM10','SMM12','SMM5','SMM6']  #Tbol increasing

	for i in range(len(sources_list_Lbol)):
		if sources_list_Lbol[i] in ['SMM1', 'SMM2', 'SMM3', 'SMM8', 'SMM9']:
			if sources_list_Lbol[i] == 'SMM3':
				ax1.text(points[0][0][i]+0.04, points[0][1][i]-0.03, sources_list_Lbol[i], fontsize=14, color='r')
				ax3.text(points[2][0][i]+0.04, points[2][1][i]-0.03, sources_list_Lbol[i], fontsize=14, color='r')
				ax5.text(points[4][0][i]+0.04, points[4][1][i]-0.03, sources_list_Lbol[i], fontsize=14, color='r')
			else:
				ax1.text(points[0][0][i]+0.02, points[0][1][i], sources_list_Lbol[i], fontsize=14, color='r')
				ax3.text(points[2][0][i]+0.02, points[2][1][i], sources_list_Lbol[i], fontsize=14, color='r')
				ax5.text(points[4][0][i]+0.02, points[4][1][i], sources_list_Lbol[i], fontsize=14, color='r')
		elif sources_list_Lbol[i] not in ['SMM1', 'SMM2', 'SMM3', 'SMM8', 'SMM9']:
			if sources_list_Lbol[i] == 'SMM4':
				ax1.text(points[0][0][i]-0.02, points[0][1][i]+0.02, sources_list_Lbol[i], fontsize=14, color='b')
				ax3.text(points[2][0][i]-0.02, points[2][1][i]+0.02, sources_list_Lbol[i], fontsize=14, color='b')
				ax5.text(points[4][0][i]-0.02, points[4][1][i]+0.02, sources_list_Lbol[i], fontsize=14, color='b')
			else:
				ax1.text(points[0][0][i]+0.02, points[0][1][i], sources_list_Lbol[i], fontsize=14, color='b')
				ax3.text(points[2][0][i]+0.02, points[2][1][i], sources_list_Lbol[i], fontsize=14, color='b')
				ax5.text(points[4][0][i]+0.02, points[4][1][i], sources_list_Lbol[i], fontsize=14, color='b')
	for i in range(len(sources_list_Tbol)):
		if sources_list_Tbol[i] in ['SMM1', 'SMM2', 'SMM3', 'SMM8', 'SMM9']:
			if sources_list_Tbol[i] == 'SMM3':
				ax2.text(points[1][0][i]+0.04, points[1][1][i]-0.01, sources_list_Tbol[i], fontsize=14, color='r')
				ax4.text(points[3][0][i]+0.04, points[3][1][i]-0.01, sources_list_Tbol[i], fontsize=14, color='r')
				ax6.text(points[5][0][i]+0.04, points[5][1][i]-0.01, sources_list_Tbol[i], fontsize=14, color='r')
			else:
				ax2.text(points[1][0][i]+0.02, points[1][1][i], sources_list_Tbol[i], fontsize=14, color='r')
				ax4.text(points[3][0][i]+0.02, points[3][1][i], sources_list_Tbol[i], fontsize=14, color='r')
				ax6.text(points[5][0][i]+0.02, points[5][1][i], sources_list_Tbol[i], fontsize=14, color='r')
		elif sources_list_Tbol[i] not in ['SMM1', 'SMM2', 'SMM3', 'SMM8', 'SMM9']:
			if sources_list_Tbol[i] == 'SMM4':
				ax2.text(points[1][0][i]-0.02, points[1][1][i]+0.02, sources_list_Tbol[i], fontsize=14, color='b')
				ax4.text(points[3][0][i]-0.02, points[3][1][i]+0.02, sources_list_Tbol[i], fontsize=14, color='b')
				ax6.text(points[5][0][i]-0.02, points[5][1][i]+0.02, sources_list_Tbol[i], fontsize=14, color='b')
			else:
				ax2.text(points[1][0][i]+0.02, points[1][1][i], sources_list_Tbol[i], fontsize=14, color='b')
				ax4.text(points[3][0][i]+0.02, points[3][1][i], sources_list_Tbol[i], fontsize=14, color='b')
				ax6.text(points[5][0][i]+0.02, points[5][1][i], sources_list_Tbol[i], fontsize=14, color='b')

	ax1.text(0.05, 0.05, 'r = '+ str(round(pearsons[0],3)) , transform=ax1.transAxes, fontsize=16, verticalalignment='bottom')
	ax2.text(0.05, 0.05, 'r = '+ str(round(pearsons[1],3)) , transform=ax2.transAxes, fontsize=16, verticalalignment='bottom')
	ax3.text(0.05, 0.05, 'r = '+ str(round(pearsons[2],3)) , transform=ax3.transAxes, fontsize=16, verticalalignment='bottom')
	ax4.text(0.05, 0.05, 'r = '+ str(round(pearsons[3],3)) , transform=ax4.transAxes, fontsize=16, verticalalignment='bottom')
	ax5.text(0.05, 0.05, 'r = '+ str(round(pearsons[4],3)) , transform=ax5.transAxes, fontsize=16, verticalalignment='bottom')
	ax6.text(0.05, 0.05, 'r = '+ str(round(pearsons[5],3)) , transform=ax6.transAxes, fontsize=16, verticalalignment='bottom')
	
	plt.savefig('Lbol_Tbol_correlations.eps', format='eps')
	plt.close()

def calculate_pearson(x, y):
	pearson = stat.pearsonr(x, y)
	#print(pearson)

	return pearson[0]

def fit_linear_regression(x, y):
	slope, intercept, r_value, p_value, stderr = stat.linregress(x,y)
	#print(slope, intercept, r_value, p_value, stderr)
	return slope, intercept, stderr

def sort_points(list_to_sort, other_list):
	if len(list_to_sort) != len(other_list):
		raise 
	merged_list = [(list_to_sort[i], other_list[i]) for i in range(len(list_to_sort))]
	sorted_list = sorted(merged_list, key=lambda x: x[0])
	return [elem[0] for elem in sorted_list], [elem[1] for elem in sorted_list]

def calculate_Lbol_for_molecule(fluxes, mol, JytoK):
	Lbol_source = []
	for i in range(len(fluxes)):
		flux_Jy_kms = fluxes[i]*JytoK # 2k/lambda^2 * T_mb [Jy*km/s]
		flux_Jy_Hz = flux_Jy_kms/((c/1000.)/freq[mol])  # F [Jy*Hz] = F [Jy*km/s] / lambda[km]
		L_bol = (1e-26*flux_Jy_Hz*4.0*m.pi*(DIST*3.0857e16)**2)/L_sun 
		#print(L_bol)
		Lbol_source.append(L_bol)

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

	Lbol_smm = [78.7, 4.1, 6.9, 4.4, 3.7, 43.1, 0.2, 10.3, 6.2, 5.7]
	Tbol_smm = [35, 31, 35, 77, 151, 532, 15, 35, 83, 97]

	points = []
	pearsons = []
	regresions = []
	
	for i in range(len(MOLECULES)):
		fluxes = create_flux_file(data, i)

		JytoK = estimate_conversion_factor(freq[i])
		Lbol_source = calculate_Lbol_for_molecule(fluxes, i, JytoK)

		Lbol, Lbol_source_1 = sort_points(Lbol_smm, Lbol_source)
		Lbol_log = make_log_list(Lbol)
		Lbol_source_log = make_log_list(Lbol_source_1)

		a, b, stderr = fit_linear_regression(Lbol_log, Lbol_source_log)
		pearson = calculate_pearson(Lbol_log, Lbol_source_log)

		points.append((Lbol_log, Lbol_source_log))
		pearsons.append(pearson)
		regresions.append((a, b))

		Tbol, Lbol_source_2 = sort_points(Tbol_smm, Lbol_source)
		Tbol_log = make_log_list(Tbol)
		Lbol_source_log = make_log_list(Lbol_source_2)

		a, b, stderr = fit_linear_regression(Tbol_log, Lbol_source_log)
		pearson = calculate_pearson(Tbol_log, Lbol_source_log)

		points.append((Tbol_log, Lbol_source_log))
		pearsons.append(pearson)
		regresions.append((a, b))
	plot_correlation(points, regresions, pearsons)
    
	#write_data('CN_Lbol_corr.txt', fluxes, a, b, pearson, stderr)
if __name__ == '__main__':
	main()
