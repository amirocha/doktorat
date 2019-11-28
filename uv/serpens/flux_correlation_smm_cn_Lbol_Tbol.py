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
			fluxes.append((line[0], float(previous_line[2]), float(line[2]), float(data[i+1].split()[2]))) # source CNflux, HCNflux, CSflux
	return fluxes

def plot_correlation(x, y, a, b, pearson):
	Y = [elem*a+b for elem in x]

	fig = plt.figure(1)
	ax = fig.add_subplot(111)
	
	ax.set_ylabel("I(CS 1-0) [K km/s]")
	ax.set_xlabel(r"T$_{\mathrm{bol}}$ [K]")

	major_ticks_x = np.arange(0, 550, 50)
	major_ticks_y = np.arange(0, 30, 2)

	ax.set_xticks(major_ticks_x)
	ax.set_yticks(major_ticks_y)

	sources_list=['SMM8','SMM2','SMM1','SMM3','SMM9','SMM4','SMM10','SMM12','SMM5','SMM6']  #Tbol increasing
	for i in range(len(sources_list)):
		ax.text(x[i]+0.2, y[i], sources_list[i])

	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)	
	ax.text(0.45, 0.05, 'Pearson coefficient = '+str(round(pearson)) , transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', bbox=props)
	
	plt.plot(x, y, 'r.', ms=4.9)
	plt.plot(x, Y, 'k-', linewidth=0.5)

	plt.savefig('CS_Tbol_correlation', format='eps')
	plt.close()

def calculate_pearson(x, y):
	pearson = stat.pearsonr(x, y)
	print(pearson)

	return pearson[0]

def make_log_list(old_list):
	new_list = []
	for elem in old_list:
		if elem != 0:
			new_list.append(m.log10(elem))
		else:
			new_list.append(elem)				

	return new_list

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
	
	Lbol = [78.7, 4.1, 6.9, 4.4, 3.7, 43.1, 0.2, 10.3, 6.2, 5.7]
	Tbol = [35, 31, 35, 77, 151, 532, 15, 35, 83, 97]

	CN_list = [point[1] for point in fluxes]
	HCN_list = [point[2] for point in fluxes]
	CS_list = [point[3] for point in fluxes]
	Tbol, CS_list = sort_points(Tbol, CS_list)

	a, b, stderr = fit_linear_regression(Tbol, CS_list)
	pearson = calculate_pearson(Tbol, CS_list)
	plot_correlation(Tbol, CS_list, a, b, pearson)
    
	#write_data('CN_Lbol_corr.txt', fluxes, a, b, pearson, stderr)
if __name__ == '__main__':
	main()
