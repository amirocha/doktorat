#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math as m
import matplotlib.pyplot as plt


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

def make_picture(new_lists):

	plt.figure()
	plt.title(u"Molecular concentrations time evolution")
	plt.ylabel(u"Log(Molecule's concentration)")
	plt.xlabel(u"Log(Time) [yr]")
	plt.plot(new_lists[0], new_lists[1], 'k-')
	plt.plot(new_lists[0], new_lists[2], 'r-')
	plt.plot(new_lists[0], new_lists[3], 'b-')
	plt.legend(('CS', 'CN', 'HCN'), loc='upper right')

	plt.savefig('concentrations', format='png')
	plt.close()

def main():

	data = read_data('plot.dat')

	time_raw = list(data[3])
	CS_raw = list(data[19])
	CN_raw = list(data[30])
	HCN_raw = list(data[52])
	lists = [time_raw, CS_raw, CN_raw, HCN_raw]

	new_lists  = remove_D(lists)
	log_lists = make_log_lists(new_lists) 
	make_picture(log_lists)

if __name__ == '__main__':
	main()
