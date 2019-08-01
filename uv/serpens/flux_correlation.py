"""Flux correlation"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat



def read_data(filename):
	file = open(filename,'r')
	data = file.readlines()
	file.close()

	return data

def write_data(end_filename, data, a, b, pearson, stderr):
	file = open(end_filename,'w')
	for CN, HCN in data:
		file.write(f'{CN:10.5} {HCN:10.5}\n')
	file.write(f'\n slope:{a:10.5} intercept:{b:10.5} stderr:{stderr:10.5} pearson:{pearson:10.5}\n')
	file.close()

def create_flux_file(CN_data, HCN_data):
	fluxes = []
	for CN_line in CN_data:
		CN_line = CN_line.split()
		for HCN_line in HCN_data:
			HCN_line = HCN_line.split()
			if CN_line[1] == HCN_line[1] and CN_line[2] == HCN_line[2]:
				fluxes.append((float(CN_line[3]), float(HCN_line[3])))
	return fluxes

def plot_correlation(x, y, a, b):
	Y = [elem*a+b for elem in x]

	fig = plt.figure(1)
	ax = fig.add_subplot(111)
	
	ax.set_xlabel("I(HCN) [K km/s]")
	ax.set_ylabel("I(CN) [K km/s]")

	major_ticks_x = np.arange(0, 15, 1)
	major_ticks_y = np.arange(0, 25, 2)

	ax.set_xticks(major_ticks_x)
	ax.set_yticks(major_ticks_y)

	plt.plot(x, y, 'r.', ms=0.9)
	plt.plot(x, Y, 'k-', linewidth=0.3)

	plt.savefig('CN_HCN_flux_correlation', format='eps')
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
	CN_data = read_data('serpens_cn10_int.txt') 
	HCN_data = read_data('serpens_hcn10_int.txt')
	fluxes = create_flux_file(CN_data, HCN_data)
	

	CN_list = [point[0] for point in fluxes]
	HCN_list = [point[1] for point in fluxes]
	HCN_list, CN_list = sort_points(HCN_list, CN_list)
	
	a, b, stderr= fit_linear_regression(CN_list, HCN_list)
	print(a, b)
	pearson = calculate_pearson(CN_list, HCN_list)
	plot_correlation(CN_list, HCN_list, a, b)

	write_data('CN_HCN_fluxes', fluxes, a, b, pearson, stderr)
    
if __name__ == '__main__':
	main()
