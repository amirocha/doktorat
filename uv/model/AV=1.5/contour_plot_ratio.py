"""Draw contour plot for chemical model parameters"""

import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Helvetica']})


time = ['1e4', '5.3e4', '1.08e5','last']
time_positions = [11, 27, 34, 124] 
molecules = ['CN', 'HCN']
mol_positions = [30, 52]
T = ['1.000D+01', '2.500D+01', '5.000D+01', '7.500D+01', '1.000D+02', '1.250D+02', '1.500D+02', '1.750D+02', '2.000D+02'] # temperature range
N = ['1.000D+04', '5.000D+04', '1.000D+05', '5.000D+05', '1.000D+06'] # H2 density range

def read_data(filename):

	file = open(filename,'r')
	data = file.readlines()
	file.close()

	return data

def remove_D(lists):

	new_lists=[]

	for old_list in lists:
		new_list = []
		for elem in old_list:
			new_elem = float(elem.replace('D', 'E'))
			new_list.append(new_elem)
		new_lists.append(new_list)

	return new_lists

def remove_D_from_elem(elem):

	new_elem = elem.replace('D', 'E')	

	return new_elem

def make_log_lists(lists):

	log_lists=[]
	for old_list in lists:
		new_list=[]
		for elem in old_list:
			if elem != 0:
				new_list.append(m.log10(elem))
			else:
				new_list.append(elem)				
		log_lists.append(new_list)	

	return log_lists

def make_picture(X, Y, Z, t):

	fig, ax = plt.subplots()
	CS = ax.contour(X, Y, Z, levels =[0.1, 0.5, 1, 3, 5, 10, 30, 50, 70, 100])
	ax.clabel(CS, inline=1, fontsize=10)
	ax.set_title(r'Chemical model parameters - CN/HCN ratio')
	plt.ylabel(r'$\log$(H$_2$ density [cm$^{-3}$])')
	plt.xlabel(u"$\log$(Temperature [K])")
	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
	ax.text(0.65, 0.85, 'AV = 1.5', transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', bbox=props)

	plt.savefig('contour_plot_CN_HCN_time='+time[t]+'.png')
	plt.close()


def main():	
	
	for t in range(len(time)):
		Z =[]
		for dens in N:
			Z_rows = []
			for temp in T:
				data = read_data('plot'+dens+'-'+temp+'.dat')
				time_position = time_positions[t]
				CN_concentration = data[30].split()[time_position]  
				CN_concentration = remove_D_from_elem(CN_concentration)
				HCN_concentration = data[52].split()[time_position] 
				HCN_concentration = remove_D_from_elem(HCN_concentration)
				concentration_ratio = float(CN_concentration)/float(HCN_concentration)
				Z_rows.append(concentration_ratio)
			Z.append(Z_rows)
		
		#Z = remove_D(Z)	
		#Z = make_log_lists(Z)
		x, y = remove_D((T, N))
		x, y = make_log_lists((x, y))
		X, Y = np.meshgrid(x, y)
		make_picture(X, Y, Z, t)
	

if __name__ == '__main__':
	main()
