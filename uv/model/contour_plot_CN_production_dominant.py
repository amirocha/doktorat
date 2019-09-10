"""Draw contour plot for chemical model parameters"""

import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Helvetica']})


DENSITIES = ['1.000E+04', '5.000E+04', '1.000E+05', '5.000E+05', '1.000E+06']
AV = ['-4.50E+00', '-3.50E+00', '-3.00E+00', '-2.50E+00', '-2.00E+00', '-1.50E+00', '-1.00E+00', '-0.50E+00', '0.000E+00', '0.500E+00', '1.000E+00', '1.500E+00', '2.00E+00', '2.500E+00', '3.000E+00']
ACTIONS = ['production', 'destruction'] 
MOLECULES = ['CN', 'HCN']
REACTIONS = [['CN_destruction', [312, 2116, 2027]], ['HCN_destruction', [589, 347, 1745, 4759]], ['CN_production', [6546, 6560, 2025, 2024]], ['HCN_production', [2043, 5046, 6811]]]
METHODS = ['ratio at 1e5 yr']

def read_data_new(filename):

	file = open(filename,'r')
	data = file.readlines()
	file.close()
	n = [] 
	G0 = []
	ratio = []
	for i in range(len(data)): 
		line=data[i].split()
		n.append(line[0])
		G0.append(line[1])
		ratio.append(line[2])
	return n, G0, ratio

def read_data(filename):

	file = open(filename,'r')
	data = file.readlines()
	file_data = []
	for line in data:
		file_data.append(' '.join(line.split()))
	file.close()

	return file_data

def freeze(d):
	if isinstance(d, dict):
		print('i')
	return frozenset((key, freeze(value)) for key, value in d.items())


def remove_D(lists):

	new_lists=[]
	for elem in old_list:
		new_elem = float(elem.replace('D', 'E'))
		new_list.append(new_elem)
	new_lists.append(new_list)

	return new_lists

def remove_D_from_elem(elem):

	new_elem = elem.replace('D', 'E')	

	return new_elem

def AV2G0(AV_list):
	
	G0_list = [m.exp(-3.12*float(av)) for av in AV_list]	#gamma coefficient taken from KIDA database for HCN + UVph -> CN + H (the newest calculations [2018-05-11] from Leiden)

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

def make_picture(grids, action, mol, reaction, method):

	fig, ax = plt.subplots()
	colours = ['red', 'blue','green', 'yellow']
	for i in range(len(grids)):
		CS = ax.contourf(grids[i][0], grids[i][1], grids[i][2], levels = [0.5, 1], colors = colours[i])
		CS = ax.contourf(grids[i][0], grids[i][1], grids[i][2], levels = [0.3, 0.5], colors = colours[i], alpha=0.5)

	#observations = ax.contourf(X, Y, Z, levels = [1,10])
	#ax.set_title(r'Chemical model parameters - CN/HCN ratio')
	plt.ylabel(r'$\log$(H$_2$ density [cm$^{-3}$])')
	plt.xlabel(r'$\log$(G$_0$)')
	#props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
	if action == 'production' and mol == 'CN':
		ax.text(-4, 5.75, r'CNC$^+$+e$^-$$\rightarrow$C+CN', fontsize=12)
		ax.text(2.5, 4.25, r'HCN$^+$+e$^-$$\rightarrow$H+CN', fontsize=12)
		ax.text(-3.5, 4.5, r'N+CH$\rightarrow$H+CN', fontsize=12)
		ax.text(-0.5, 5.55, r'N+C$_2$$\rightarrow$C+CN', fontsize=12)
	if action == 'production' and mol == 'HCN':
		ax.text(-3.7, 5.5, r'N+CH$_2$$\rightarrow$H+HCN', fontsize=12)
		ax.text(0, 5.75, r'H+CCN$\rightarrow$C+HCN', fontsize=12)
		ax.text(1, 4.75, r'HCNH$^+$+e$^-$$\rightarrow$H+HCN', fontsize=12)
	if action == 'destruction' and mol == 'CN':
		ax.text(-3., 4.56, r'O+CN$\rightarrow$N+CO', fontsize=12)
		ax.text(2, 5., r'CN+ph$\rightarrow$C+N', fontsize=12)
		ax.text(-3.2, 5.75, r'CN+N$\rightarrow$C+N$_2$', fontsize=12)
	if action == 'destruction' and mol == 'HCN':
		ax.text(-2, 5., r'HCN+C$^+$$\rightarrow$H+CNC$^+$', fontsize=12)
		ax.text(2.5, 4.75, r'HCN+ph$\rightarrow$H+CN', fontsize=12)
		ax.text(-5., 4.1, r'HCN+H$^+$$\rightarrow$H+HNC$^+$', fontsize=12)
		ax.text(-5.5, 5.85, r'HCN$^+$+HCO$^+$$\rightarrow$CO+HCNH$^+$', fontsize=12)
	plt.savefig(action+'_'+mol+'_dominant.eps')
	plt.close()


def main():
	
	for action in ACTIONS:
		for mol in MOLECULES:
			for i in range(len(REACTIONS)):
				grids = []
				if REACTIONS[i][0] == mol+'_'+action:
					for reaction in REACTIONS[i][1][0:]:
						reaction = str(reaction)
						for method in METHODS:
							#n, G0, ratio = read_data(action+'_'+mol+'_'+reaction+'_'+method)
							file_data = read_data(action+'_'+mol+'_'+reaction+'_'+method)
							Z = []
							new_list = []
							for i in range(len(DENSITIES)):
								Z_row = []
								
								for j in range(len(AV)):
									position = f'{DENSITIES[i]} {AV[j]}'
									present = False
									for k in range(len(file_data)):
										if file_data[k].startswith(position):
											Z_row.append(float(file_data[k].split()[2]))
											present = True
											break
										if k == len(file_data)-1 and present == False:
											Z_row.append(0)
								Z.append(Z_row)
							x = AV2G0(AV)
							DENSITIES_floats = []
							for dens in DENSITIES:
								DENSITIES_floats.append(float(dens))
							x, y = make_log_lists((x, DENSITIES_floats))
							X, Y = np.meshgrid(x, y)
							grids.append((X, Y, Z))
					make_picture(grids, action, mol, reaction, method)

if __name__ == '__main__':
	main()
