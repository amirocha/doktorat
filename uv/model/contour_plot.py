"""Draw contour plot for chemical model parameters"""

import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Helvetica']})


time = ['1e4', '5.3e4', '1.08e5']
time_positions = [11, 27, 34] 
molecules = ['CS', 'CN', 'HCN', 'H2']
mol_positions = [19, 30, 52, 28]
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

def make_picture(X, Y, Z, m, t):

	fig, ax = plt.subplots()
	CS = ax.contour(X, Y, Z)
	ax.clabel(CS, inline=1, fontsize=10, fmt = '%.2E')
	ax.set_title(r'Chemical model parameters - '+molecules[m])
	plt.ylabel(r'$\log$(H$_2$ density [cm$^{-3}$])')
	plt.xlabel(u"$\log$(Temperature [K])")
	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
	ax.text(0.65, 0.85, 'Time = '+time[t] , transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', bbox=props)

	plt.savefig('contour_plot_'+molecules[m]+'_time='+time[t], format='png')
	plt.close()


def main():	
	for m in range(len(molecules)):
		for t in range(len(time)):
			Z =[]
			for dens in N:
				Z_rows = []
				for temp in T:
					data = read_data('plot'+dens+'-'+temp+'.dat')
					#reading from 'output.dat': mol_concentration = data[26].split()[16]   //28 for CN; 50 for HCN; 17 for CS; 26 for H2
					time_position = time_positions[t]
					mol_position = mol_positions[m]
					mol_concentration = data[mol_position].split()[time_position]  #reading from plot.dat: 19 for CS; 30 for CN; 52 for HCN; 28 for H2//time: 11 for 1e4; 27 for 5.3e4; 34 for 1.08e5
					Z_rows.append(mol_concentration)
				Z.append(Z_rows)
			Z = remove_D(Z)	
			#Z = make_log_lists(Z)
			x, y = remove_D((T, N))
			x, y = make_log_lists((x, y))
			X, Y = np.meshgrid(x, y)
			make_picture(X, Y, Z, m, t)
	

if __name__ == '__main__':
	main()
