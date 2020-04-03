"""Draw contour plot for chemical model parameters"""

import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Helvetica']})
import matplotlib.ticker as ticker



AV = ['-4.50D+00', '-4.00D+00', '-3.50D+00', '2.500D+00', '1.500D+00', '0.500D+00', '-0.50D+00', '-1.50D+00', '-2.50D+00', '2.000D+00', '1.000D+00', '0.000D+00', '-1.00D+00', '-2.00D+00', '-3.00D+00']
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

def AV2G0(AV_list):

	G0_list = [m.exp(-3.12*av) for av in AV_list]	#gamma coefficient taken from KIDA database for HCN + UVph -> CN + H (the newest calculations [2018-05-11] from Leiden)

	return G0_list

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

def make_picture(X, Y, Z):

	fig, ax = plt.subplots()
	CS = ax.contour(X, Y, Z)
	ax.clabel(CS, inline=1, fontsize=10, fmt=ticker.LogFormatterMathtext())
	#observations = ax.contourf(X, Y, Z, levels = [1,10])
	ax.set_title(r'Chemical model parameters - CO abundances')
	plt.ylabel(r'$\log$(H$_2$ density [cm$^{-3}$])')
	plt.xlabel(r'$\log$(G$_0$)')
	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
	ax.text(0.80, 0.1, 'T = 200K', transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', bbox=props)

	plt.savefig('contour_plot_CO_200K.eps')
	plt.close()


def main():
	
	Z = []
	AV_E = []
	for av in AV:
		av_E = av.replace('D','E')
		AV_E.append(float(av_E))

	AV_E.sort()

	for dens in N:
		Z_rows = []
		i = 0
		for av in AV:
			av = AV[i]
			data_new = read_data('./plot'+dens+'-'+av+'.dat')
			time_position = 124  
			C_abudance = data_new[20].split()[time_position]  
			C_abudance = remove_D_from_elem(C_abudance)
			Z_rows.append(C_abudance)
			i += 1
		Z.append(Z_rows)
	x0, y = remove_D((T, N))
	x = AV2G0(AV_E)
	x, y = make_log_lists((x, y))
	X, Y = np.meshgrid(x, y)
	make_picture(X, Y, Z)
	

if __name__ == '__main__':
	main()

'''
CO - 20
C - 7
O - 
CN - 30
H - 6

'''
