"""Draw contour plot for chemical model parameters"""

import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Helvetica']})



AV = [-1.0, 0.0, 1.0, 1.5, 2.0]

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
	CS = ax.contour(X, Y, Z, levels = [0.01, 0.1, 1, 10, 100, 1000, 10000])
	ax.clabel(CS, inline=1, fontsize=10)
	observations = ax.contourf(X, Y, Z, levels = [0.1,0.3])
	#ax.set_title(r'Chemical model parameters - CS/HCN ratio')
	plt.ylabel(r'$\log$(H$_2$ density [cm$^{-3}$])')
	plt.xlabel(r'$\log$(G$_0$)')
	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
	ax.text(4.25, 4.15, '$T$ = 50K', fontsize=14, verticalalignment='bottom', bbox=props)
	ax.text(4.5, 5.75, r'$\frac{X(CS)}{X(HCN)}$', fontsize=18, color='k', bbox=props)

	plt.savefig('CS_HCN.eps')
	plt.close()


def main():
	
	Z = []
	AV_new_E = []


	for dens in N:
		Z_rows = []
		i = 0
		for av in AV:
			if av in AV:
				data = read_data('./AV='+str(av)+'/plot'+dens+'-5.000D+01.dat')
				time_position = 124  
				CS_abudance = data[19].split()[time_position]  
				CS_abudance = remove_D_from_elem(CS_abudance)
				HCN_abudance = data[52].split()[time_position] 
				HCN_abudance = remove_D_from_elem(HCN_abudance)
				abudance_ratio = float(CS_abudance)/float(HCN_abudance)
				Z_rows.append(abudance_ratio)
			elif av not in AV:
				av_new = AV_new[i]
				data_new = read_data('./plot'+dens+'-'+av_new+'.dat')
				time_position = 124  
				CS_abudance_new = data_new[19].split()[time_position]  
				CS_abudance_new = remove_D_from_elem(CS_abudance_new)
				HCN_abudance_new = data_new[52].split()[time_position] 
				HCN_abudance_new = remove_D_from_elem(HCN_abudance_new)
				abudance_ratio_new = float(CS_abudance_new)/float(HCN_abudance_new)
				Z_rows.append(abudance_ratio_new)
				i += 1
		Z.append(Z_rows)
	x0, y = remove_D((T, N))
	x = AV2G0(AV)
	x, y = make_log_lists((x, y))
	X, Y = np.meshgrid(x, y)
	make_picture(X, Y, Z)
	

if __name__ == '__main__':
	main()
