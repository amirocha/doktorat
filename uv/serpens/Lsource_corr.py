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
	fig = plt.figure(figsize = (10,15), dpi = 400)
	plt.tick_params(axis='y', which='both', right=False)
	fig.subplots_adjust(hspace=0.4)

	ax1 = plt.subplot(3, 1, 1)
	# Set the tick labels font
	for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
	#    label.set_fontname('Arial')
   		label.set_fontsize(20)
	ax1.set_xlim([-6, -5.1])
	ax1.set_ylim([-6, -5.1])
	plt.plot(points[0][0], points[0][1], 'k.', ms=10)
	Y = [elem*regresions[0][0]+regresions[0][1] for elem in points[0][0]]
	plt.plot(points[0][0], Y, 'k-', linewidth=0.8)

	ax2 = plt.subplot(3, 1, 2)
	for label in (ax2.get_xticklabels() + ax2.get_yticklabels()):
	#    label.set_fontname('Arial')
   		label.set_fontsize(20)
	ax2.set_xlim([-6, -5.1])
	ax2.set_ylim([-5.7, -4.8])
	plt.plot(points[1][0], points[1][1], 'k.', ms=10)
	Y = [elem*regresions[1][0]+regresions[1][1] for elem in points[1][0]]
	plt.plot(points[1][0], Y, 'k-', linewidth=0.8)

	ax3 = plt.subplot(3, 1, 3)
	for label in (ax3.get_xticklabels() + ax3.get_yticklabels()):
	#    label.set_fontname('Arial')
   		label.set_fontsize(20)
	ax3.set_xlim([-6, -5.1])
	ax3.set_ylim([-5.7, -4.8])
	plt.plot(points[2][0], points[2][1], 'k.', ms=10)
	Y = [elem*regresions[2][0]+regresions[2][1] for elem in points[2][0]]
	plt.plot(points[2][0], Y, 'k-', linewidth=0.8)

	
	ax1.set_ylabel(r"$L_{\mathrm{CN}}$ [L$_\odot$]", fontsize=24)
	ax1.set_xlabel(r"$L_{\mathrm{HCN}}$ [L$_\odot$]", fontsize=24)
	ax2.set_ylabel(r"$L_{\mathrm{CN}}$ [L$_\odot$]", fontsize=24)
	ax2.set_xlabel(r"$L_{\mathrm{CS}}$ [L$_\odot$]", fontsize=24)
	ax3.set_ylabel(r"$L_{\mathrm{HCN}}$ [L$_\odot$]", fontsize=24)
	ax3.set_xlabel(r"$L_{\mathrm{CS}}$ [L$_\odot$]", fontsize=24) 

	sources_list_CN = ['SMM5','SMM10','SMM8','SMM9','SMM1','SMM2','SMM12','SMM4','SMM6','SMM3']  #in respect order in CN luminosity
	sources_list_HCN = ['SMM5','SMM8','SMM10','SMM1','SMM2','SMM6','SMM12','SMM3','SMM9','SMM4']  #in respect order in CN luminosity

	for i in range(len(sources_list_CN)):
		if sources_list_CN[i] in ['SMM1', 'SMM2', 'SMM3', 'SMM8', 'SMM9']:
				if sources_list_CN[i] == 'SMM8':
					ax1.text(points[0][0][i]+0.01, points[0][1][i]-0.04, sources_list_CN[i], fontsize=18, color='r')
					ax2.text(points[1][0][i]+0.01, points[1][1][i]-0.04, sources_list_CN[i], fontsize=18, color='r')
				elif sources_list_CN[i] == 'SMM3':
					ax1.text(points[0][0][i]+0.03, points[0][1][i]-0.0, sources_list_CN[i], fontsize=18, color='r')
					ax2.text(points[1][0][i]+0.03, points[1][1][i]-0.0, sources_list_CN[i], fontsize=18, color='r')
				else:
					ax1.text(points[0][0][i]+0.01, points[0][1][i]-0.0, sources_list_CN[i], fontsize=18, color='r')
					ax2.text(points[1][0][i]+0.01, points[1][1][i]-0.0, sources_list_CN[i], fontsize=18, color='r')
			
		elif sources_list_CN[i] not in ['SMM1', 'SMM2', 'SMM3', 'SMM8', 'SMM9']:
				if sources_list_CN[i] == 'SMM6':
					ax1.text(points[0][0][i]+0.01, points[0][1][i]-0.02, sources_list_CN[i], fontsize=18, color='b')
					ax2.text(points[1][0][i]+0.01, points[1][1][i]-0.02, sources_list_CN[i], fontsize=18, color='b')
				else:
					ax1.text(points[0][0][i]+0.01, points[0][1][i]-0.0, sources_list_CN[i], fontsize=18, color='b')
					ax2.text(points[1][0][i]+0.01, points[1][1][i]+0.0, sources_list_CN[i], fontsize=18, color='b')

	for i in range(len(sources_list_HCN)):
		if sources_list_HCN[i] in ['SMM1', 'SMM2', 'SMM3', 'SMM8', 'SMM9']:
				if sources_list_HCN[i] == 'SMM2':
					ax3.text(points[2][0][i]-0.08, points[2][1][i]-0.01, sources_list_HCN[i], fontsize=18, color='r')
				elif sources_list_HCN[i] == 'SMM3':
					ax3.text(points[2][0][i]+0.01, points[2][1][i]-0.03, sources_list_HCN[i], fontsize=18, color='r')
				else:
					ax3.text(points[2][0][i]+0.01, points[2][1][i]-0.01, sources_list_HCN[i], fontsize=18, color='r')
			
		elif sources_list_HCN[i] not in ['SMM1', 'SMM2', 'SMM3', 'SMM8', 'SMM9']:
				ax3.text(points[2][0][i]+0.01, points[2][1][i]+0.0, sources_list_HCN[i], fontsize=18, color='b')
					
				
				

	ax1.text(0.80, 0.05, 'r = '+ str(round(pearsons[0],2)) , transform=ax1.transAxes, fontsize=22, verticalalignment='bottom')
	ax2.text(0.80, 0.05, 'r = '+ str(round(pearsons[1],2)) , transform=ax2.transAxes, fontsize=22, verticalalignment='bottom')
	ax3.text(0.80, 0.05, 'r = '+ str(round(pearsons[2],2)) , transform=ax3.transAxes, fontsize=22, verticalalignment='bottom')
	
	plt.savefig('Lsources_correlations.eps', format='eps')
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
		if i == 0:
			Lbol_CN = calculate_Lbol_for_molecule(fluxes, i, JytoK)
		elif i == 1:
			Lbol_HCN = calculate_Lbol_for_molecule(fluxes, i, JytoK)
		elif i == 2:
			Lbol_CS = calculate_Lbol_for_molecule(fluxes, i, JytoK)
	
	Lbol_CN_log = make_log_list(Lbol_CN)
	Lbol_HCN_log = make_log_list(Lbol_HCN)	
	Lbol_CS_log = make_log_list(Lbol_CS)
	Lbol_CN_1, Lbol_HCN_1 = sort_points(Lbol_CN_log, Lbol_HCN_log)
	Lbol_CN_2, Lbol_CS_2 = sort_points(Lbol_CN_log, Lbol_CS_log)
	Lbol_HCN_3, Lbol_CS_3 = sort_points(Lbol_HCN_log, Lbol_CS_log)

	a, b, stderr = fit_linear_regression(Lbol_CN_1, Lbol_HCN_1)
	pearson = calculate_pearson(Lbol_CN_1, Lbol_HCN_1)

	points.append((Lbol_CN_1, Lbol_HCN_1))
	pearsons.append(pearson)
	regresions.append((a, b))

	a, b, stderr = fit_linear_regression(Lbol_CN_2, Lbol_CS_2)
	pearson = calculate_pearson(Lbol_CN_2, Lbol_CS_2)

	points.append((Lbol_CN_2, Lbol_CS_2))
	pearsons.append(pearson)
	regresions.append((a, b))

	a, b, stderr = fit_linear_regression(Lbol_HCN_3, Lbol_CS_3)
	pearson = calculate_pearson(Lbol_HCN_3, Lbol_CS_3)

	points.append((Lbol_HCN_3, Lbol_CS_3))
	pearsons.append(pearson)
	regresions.append((a, b))

	plot_correlation(points, regresions, pearsons)
    
	#write_data('CN_Lbol_corr.txt', fluxes, a, b, pearson, stderr)
if __name__ == '__main__':
	main()
