"""Flux correlation"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat



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

def create_flux_file(data):
	fluxes = []
	for i in range(1,len(data)):
		line = data[i].split()
		previous_line = data[i-1].split()
		if line[1] == 'hcn10' and previous_line[1] == 'cn10':
			fluxes.append((line[0], float(previous_line[2]), float(line[2])))
	return fluxes

def plot_correlation(x, y, a, b):
	Y = [elem*a+b for elem in x]

	fig = plt.figure(1)
	ax = fig.add_subplot(111)
	
	ax.set_xlabel("I(HCN J=1-0) [K km/s]")
	ax.set_ylabel("I(CN J=1-0) [K km/s]")

	major_ticks_x = np.arange(0, 25, 1)
	major_ticks_y = np.arange(0, 15, 2)

	ax.set_xticks(major_ticks_x)
	ax.set_yticks(major_ticks_y)

	sources_list=['SMM5','SMM8','SMM10','SMM1','SMM2','SMM12','SMM6','SMM9','SMM3','SMM4']
	for i in range(len(sources_list)):
		ax.text(x[i]+0.2, y[i], sources_list[i])

	plt.plot(x, y, 'r.', ms=4.9)
	plt.plot(x, Y, 'k-', linewidth=0.5)

	plt.savefig('CN_HCN_flux_correlation_smm', format='eps')
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
    
	write_data('CN_HCN_corr_smm', fluxes, a, b, pearson, stderr)
if __name__ == '__main__':
	main()
