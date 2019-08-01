"""Flux correlation"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Helvetica']})

def read_data(filename):
	file = open(filename,'r')
	data = file.readlines()
	file.close()

	return data

def write_data(end_filename, data, a, b, pearson, stderr):
	file = open(end_filename,'w')
	for SMM, CN, HCN in data:
		file.write(f'{SMM:10.5} {CN:10.5} {HCN:10.5}\n')
	file.write(f'\n slope:{a:10.5} intercept:{b:10.5} stderr:{stderr:10.5} pearson:{pearson:10.5}\n')
	file.close()

def create_flux_file(data):
	fluxes = []
	for i in range(1,len(data)):
		line = data[i].split()
		previous_line = data[i-1].split()
		if line[1] == 'c34s32' and previous_line[1] == 'cs32':
			fluxes.append((line[0], float(line[2]), float(previous_line[2])))
	print(fluxes)
	return fluxes

def plot_correlation(x, y, a, b):
	Y = [elem*a+b for elem in x]

	fig = plt.figure(1)
	ax = fig.add_subplot(111)
	
	ax.set_ylabel(r"I(C$^{34}$S J=3-2) [K km/s]")
	ax.set_xlabel("I(CS J=3-2) [K km/s]")

	major_ticks_x = np.arange(0, 25, 1)
	major_ticks_y = np.arange(0, 1.6, 0.2)

	ax.set_xticks(major_ticks_x)
	ax.set_yticks(major_ticks_y)

	sources_list=['SMM5','SMM1','SMM10','SMM8','SMM2','SMM6','SMM3','SMM12','SMM9','SMM4']
	for i in range(len(sources_list)):
		ax.text(x[i]-0, y[i]+0, sources_list[i])
		#ax.text(x[6]-1.5, y[6]+0, 'SMM12')
		#ax.text(x[7], y[7], 'SMM6')

	plt.plot(x, y, 'r.', ms=4.9)
	plt.plot(x, Y, 'k-', linewidth=0.5)

	plt.savefig('C34S_CS_flux_correlation_smm', format='eps')
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

def main():
	data = read_data('SMM_fluxes') 
	fluxes = create_flux_file(data)

	CN_list = [point[1] for point in fluxes]
	HCN_list = [point[2] for point in fluxes]
	HCN_list, CN_list = sort_points(HCN_list, CN_list)

	a, b, stderr = fit_linear_regression(HCN_list, CN_list)
	print(a, b)
	pearson = calculate_pearson(HCN_list, CN_list)
	plot_correlation(HCN_list, CN_list, a, b)

	write_data('C34S_CS_corr_smm', fluxes, a, b, pearson, stderr)
    
if __name__ == '__main__':
	main()
