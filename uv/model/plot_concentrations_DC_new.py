#!/usr/bin/python3.3


# import packages
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import *
import math as m

#fig = plt.figure(figsize = (5,8), dpi = 400)


rc('font', **{'family':'serif', 'serif':['Times New Roman']})
params = {'backend': 'pdf',
          'axes.labelsize': 12,
          #'text.fontsize': 12,
          #'legend.fontsize': 12,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10,
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

def read_data(filename):

	file = open(filename,'r')
	data = file.readlines()
	file.close()

	return data

def remove_D(lists):

	new_lists=[]

	for old_list in lists:
		
		for n, i in enumerate(old_list):
			if i == 'D':
				old_list[n] = 'E'
		new_list = []

		if old_list[0] == 'C':
			old_list = old_list[2:]
		
		if old_list[0] == 'H':
			old_list = old_list[3:]

		old_list = ''.join(old_list).split()

		for elem in old_list:
			new_elem = float(elem)
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

def remove_first_step(lists):
	
	for one_list in lists:
		one_list.pop(0)
	
	return lists


def make_picture(new_lists):

	plt.figure()
	#plt.title(u"Molecular abudances time evolution")
	plt.ylabel(r"$\log(\frac{N(X)}{N(H_2)})$", fontsize=14)
	plt.xlabel(r"$\log(t/yr)$", fontsize=14)
	plt.plot(new_lists[0], new_lists[1], 'k-')
	plt.plot(new_lists[0], new_lists[2], 'r-')
	plt.plot(new_lists[0], new_lists[3], 'b-')
	#plt.legend(('CS', 'CN', 'HCN'), loc='upper right')
	plt.text(7., -4., 'HCN', fontsize=14, color='b')
	plt.text(7., -5, 'CN', fontsize=14, color='r')
	plt.text(7., -6, 'CS', fontsize=14, color='k')

	plt.savefig('concentrations_DC_new', format='eps')
	plt.close()

def main():

	data = read_data('plot_DC.dat')

	time_raw = list(data[3])
	CS_raw = list(data[19])
	CN_raw = list(data[30])
	HCN_raw = list(data[52])

	lists = [time_raw, CS_raw, CN_raw, HCN_raw]

	new_lists  = remove_D(lists)
	log_lists = make_log_lists(new_lists) 
	#shorter_log_lists = remove_first_step(log_lists)
	make_picture(log_lists)

if __name__ == '__main__':
	main()
