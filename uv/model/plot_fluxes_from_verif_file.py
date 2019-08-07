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

def write_to_file(end_filename, density, G0, ratio):
	file = open(end_filename,'w')
	file.write(f'{density} {G0} {ratio}\n')

	file.close()

def append_to_file(end_filename, density, G0, ratio):
	file = open(end_filename,'a')
	file.write(f'{density} {G0} {ratio}\n')

	file.close()

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

def make_picture(lists, point, reaction_lists, keyword):

	plt.figure()
	plt.title(u"Time evolution of "+keyword)
	plt.ylabel(u"Log(Reaction fluxes)")
	plt.xlabel(u"Log(Time) [yr]")
	colours = ['','k-', 'r-', 'b-', 'm-', 'g-', 'c-', 'orangered']
	for i in range(1, len(lists)):
		plt.plot(lists[0], lists[i], colours[i])
	legend = ['total']
	for reaction in reaction_lists:
		legend.append(reaction)
	plt.legend(legend, loc='upper right')

	plt.savefig(keyword+'_'+str(point)+'.png', format='png')
	plt.close()

def read_times():
	file = open('timeres.dat','r')
	raw_data = file.readlines()
	data = []
	for line in raw_data:
		elem = line.split()[0]
		data.append(float(elem))
	data.pop(0)
	file.close()

	return data

def transpone_matrix(lists):
	first_list = []
	second_list = []
	for i in range(len(lists)):
		first_list.append(lists[i][0])
		second_list.append(lists[i][1])

	return (first_list, second_list)

def limit_lists(lists):
	time_list = lists[0]
	reference_list = lists[1]
	list_10e4yr = []
	list_10e5yr = []
	list_integrals = []
	list_int_reference = []
	for j in range(2,len(lists)):
		list_int = []
		time_int = []
		for i in range(len(time_list)):
			if time_list[i] == 10800:   #points at 10^4yrs of evolution
				elem = lists[j][i]/reference_list[i]
				list_10e4yr.append((elem, j))
			if time_list[i] == 102100:   #points at 10^5yrs of evolution
				elem = lists[j][i]/reference_list[i]
				list_10e5yr.append((elem, j))
			if time_list[i] < 50000:     #integration in range [0, 5e12^4]
				time_int.append(time_list[i])
				list_int.append(lists[j][i])
				list_int_reference.append(reference_list[i])
		integral = integrate(time_int, list_int)
		integral_ref = integrate(time_int, list_int_reference)
		list_integrals.append((integral/integral_ref, j))
	
	list_10e4yr_sorted = sort_points(transpone_matrix(list_10e4yr)[0],transpone_matrix(list_10e4yr)[1])
	list_10e5yr_sorted = sort_points(transpone_matrix(list_10e5yr)[0],transpone_matrix(list_10e5yr)[1])
	list_integrals_sorted = sort_points(transpone_matrix(list_integrals)[0],transpone_matrix(list_integrals)[1])

	limited_list_10e4yr = []
	limited_list_10e5yr = []
	limited_list_int = []

	ratio = list_10e4yr_sorted[0][0]  
	for i in range(len(list_10e4yr_sorted[0])-1):
		if ratio > 0.8: 
			limited_list_10e4yr.append((list_10e4yr_sorted[0][i], list_10e4yr_sorted[1][i]))
			break
		else:
			limited_list_10e4yr.append((list_10e4yr_sorted[0][i], list_10e4yr_sorted[1][i]))
			ratio+=list_10e4yr_sorted[0][i+1]
	
	ratio = list_10e5yr_sorted[0][0]  
	for i in range(len(list_10e5yr_sorted[0])-1):
		if ratio > 0.8: 
			limited_list_10e5yr.append((list_10e5yr_sorted[0][i], list_10e5yr_sorted[1][i]))
			break
		else:
			limited_list_10e5yr.append((list_10e5yr_sorted[0][i], list_10e5yr_sorted[1][i]))
			ratio+=list_10e5yr_sorted[0][i+1]

	ratio = list_integrals_sorted[0][0]	
	for i in range(len(list_integrals_sorted[0])-1):
		if ratio > 0.8: 
			limited_list_int.append((list_integrals_sorted[0][i], list_integrals_sorted[1][i]))
			break
		else:
			limited_list_int.append((list_integrals_sorted[0][i], list_integrals_sorted[1][i]))
			ratio+=list_integrals_sorted[0][i+1]

	limited_reactions = [limited_list_10e4yr, limited_list_10e5yr, limited_list_int]

	return limited_reactions

def integrate(x,y):
	integral=0
	for i in range(len(x)-1):
		integral+=y[i]*(x[i+1]-x[i])
	return integral

def sort_points(list_to_sort, other_list):
	if len(list_to_sort) != len(other_list):
		raise 
	merged_list = [(list_to_sort[i], other_list[i]) for i in range(len(list_to_sort))]
	sorted_list = sorted(merged_list, key=lambda x: x[0], reverse = True) #from the highest value
	return [elem[0] for elem in sorted_list], [elem[1] for elem in sorted_list]

def main():
	time = read_times()
	writed_reactions_prod = []
	writed_reactions_dest = []
	
	for density in ['1.000E+04', '5.000E+04', '1.000E+05', '5.000E+05', '1.000E+06']:
		for G0 in ['-4.50E+00', '-3.50E+00', '2.500E+00', '1.500E+00', '0.500E+00', '-0.50E+00', '-1.50E+00', '-2.50E+00', '3.000E+00', '2.00E+00', '1.000E+00', '0.000E+00', '-1.00E+00', '-2.00E+00', '-3.00E+00']:
			#print(density, G0)
			density_D = density.replace('E','D')
			G0_D = G0.replace('E','D')
			data = read_data('verif'+density_D+'-'+G0_D+'.dat')
			
			CN_prod_tot = []
			CN_prod_1 = [] #first reaction from production list
			CN_prod_2 = []
			CN_prod_3 = []
			CN_prod_4 = []
			CN_prod_5 = []
			CN_prod_6 = [] 
			CN_prod_7 = []
			CN_prod_8 = []
			CN_prod_9 = []
			CN_prod_10 = []
			CN_dest_tot = []
			CN_dest_1 = [] #first reaction from destruction list
			CN_dest_2 = []
			CN_dest_3 = []
			CN_dest_4 = []
			CN_dest_5 = []
			CN_dest_6 = [] 
			CN_dest_7 = []
			CN_dest_8 = []
			CN_dest_9 = []
			CN_dest_10 = []

			HCN_prod_tot = []
			HCN_prod_1 = [] #first reaction from production list
			HCN_prod_2 = []
			HCN_prod_3 = []
			HCN_prod_4 = []
			HCN_prod_5 = []
			HCN_prod_6 = [] 
			HCN_prod_7 = []
			HCN_prod_8 = []
			HCN_prod_9 = []
			HCN_prod_10 = []
			HCN_dest_tot = []
			HCN_dest_1 = [] #first reaction from destruction list
			HCN_dest_2 = []
			HCN_dest_3 = []
			HCN_dest_4 = []
			HCN_dest_5 = []
			HCN_dest_6 = [] 
			HCN_dest_7 = []
			HCN_dest_8 = []
			HCN_dest_9 = []
			HCN_dest_10 = []
			for i in range(1,len(time)-1):
				
				CN_tot_flux = float(data[602 + i*11250].split()[7]) 
				CN_prod_tot.append(('production_tot', CN_tot_flux))
				CN_prod_1_reaction =  data[603 + i*11250].split()[0] 
				CN_prod_1_flux = float(data[603 + i*11250].split()[1]) 
				CN_prod_1.append((CN_prod_1_reaction, CN_prod_1_flux))
				CN_prod_2_reaction =  data[604 + i*11250].split()[0] 
				CN_prod_2_flux = float(data[604 + i*11250].split()[1]) 
				CN_prod_2.append((CN_prod_2_reaction, CN_prod_2_flux))
				CN_prod_3_reaction =  data[605 + i*11250].split()[0] 
				CN_prod_3_flux = float(data[605 + i*11250].split()[1]) 
				CN_prod_3.append((CN_prod_3_reaction, CN_prod_3_flux))
				CN_prod_4_reaction =  data[606 + i*11250].split()[0] 
				CN_prod_4_flux = float(data[606 + i*11250].split()[1]) 
				CN_prod_4.append((CN_prod_4_reaction, CN_prod_4_flux))
				CN_prod_5_reaction =  data[607 + i*11250].split()[0] 
				CN_prod_5_flux = float(data[607 + i*11250].split()[1]) 
				CN_prod_5.append((CN_prod_5_reaction, CN_prod_5_flux))
				CN_prod_6_reaction =  data[608 + i*11250].split()[0] 
				CN_prod_6_flux = float(data[608 + i*11250].split()[1]) 
				CN_prod_6.append((CN_prod_6_reaction, CN_prod_6_flux))
				CN_prod_7_reaction =  data[609 + i*11250].split()[0] 
				CN_prod_7_flux = float(data[609 + i*11250].split()[1]) 
				CN_prod_7.append((CN_prod_7_reaction, CN_prod_7_flux))
				CN_prod_8_reaction =  data[610 + i*11250].split()[0] 
				CN_prod_8_flux = float(data[610 + i*11250].split()[1]) 
				CN_prod_8.append((CN_prod_8_reaction, CN_prod_8_flux))
				CN_prod_9_reaction =  data[611 + i*11250].split()[0] 
				CN_prod_9_flux = float(data[611 + i*11250].split()[1]) 
				CN_prod_9.append((CN_prod_9_reaction, CN_prod_9_flux))
				CN_prod_10_reaction =  data[612 + i*11250].split()[0] 
				CN_prod_10_flux = float(data[612 + i*11250].split()[1]) 
				CN_prod_10.append((CN_prod_10_reaction, CN_prod_10_flux))
				CN_tot_flux = float(data[613 + i*11250].split()[7]) 
				CN_dest_tot.append(('destruction_tot', CN_tot_flux))
				CN_dest_1_reaction =  data[614 + i*11250].split()[0] 
				CN_dest_1_flux = abs(float(data[614 + i*11250].split()[1])) 
				CN_dest_1.append((CN_dest_1_reaction, CN_dest_1_flux))
				CN_dest_2_reaction =  data[615 + i*11250].split()[0] 
				CN_dest_2_flux = abs(float(data[615 + i*11250].split()[1])) 
				CN_dest_2.append((CN_dest_2_reaction, CN_dest_2_flux))
				CN_dest_3_reaction =  data[616 + i*11250].split()[0] 
				CN_dest_3_flux = abs(float(data[616 + i*11250].split()[1])) 
				CN_dest_3.append((CN_dest_3_reaction, CN_dest_3_flux))
				CN_dest_4_reaction =  data[617 + i*11250].split()[0] 
				CN_dest_4_flux = abs(float(data[617 + i*11250].split()[1])) 
				CN_dest_4.append((CN_dest_4_reaction, CN_dest_4_flux))
				CN_dest_5_reaction =  data[618 + i*5467].split()[0] 
				CN_dest_5_flux = abs(float(data[618 + i*11250].split()[1])) 
				CN_dest_5.append((CN_dest_5_reaction, CN_dest_5_flux))
				CN_dest_6_reaction =  data[619 + i*11250].split()[0] 
				CN_dest_6_flux = abs(float(data[619 + i*11250].split()[1])) 
				CN_dest_6.append((CN_dest_6_reaction, CN_dest_6_flux))
				CN_dest_7_reaction =  data[620 + i*11250].split()[0] 
				CN_dest_7_flux = abs(float(data[620 + i*11250].split()[1])) 
				CN_dest_7.append((CN_dest_7_reaction, CN_dest_7_flux))
				CN_dest_8_reaction =  data[621 + i*11250].split()[0] 
				CN_dest_8_flux = abs(float(data[621 + i*11250].split()[1])) 
				CN_dest_8.append((CN_dest_8_reaction, CN_dest_8_flux))
				CN_dest_9_reaction =  data[622 + i*11250].split()[0] 
				CN_dest_9_flux = abs(float(data[622 + i*11250].split()[1])) 
				CN_dest_9.append((CN_dest_9_reaction, CN_dest_9_flux))
				CN_dest_10_reaction =  data[623 + i*11250].split()[0] 
				CN_dest_10_flux = abs(float(data[623 + i*11250].split()[1])) 
				CN_dest_10.append((CN_dest_10_reaction, CN_dest_10_flux))
				
				HCN_tot_flux = float(data[1108 + i*11250].split()[7]) 
				HCN_prod_tot.append(('production tot', HCN_tot_flux))
				HCN_prod_1_reaction =  data[1109 + i*11250].split()[0] 
				HCN_prod_1_flux = float(data[1109 + i*11250].split()[1]) 
				HCN_prod_1.append((HCN_prod_1_reaction, HCN_prod_1_flux))
				HCN_prod_2_reaction =  data[1110 + i*11250].split()[0] 
				HCN_prod_2_flux = float(data[1110 + i*11250].split()[1]) 
				HCN_prod_2.append((HCN_prod_2_reaction, HCN_prod_2_flux))
				HCN_prod_3_reaction =  data[1111 + i*11250].split()[0] 
				HCN_prod_3_flux = float(data[1111 + i*11250].split()[1]) 
				HCN_prod_3.append((HCN_prod_3_reaction, HCN_prod_3_flux))
				HCN_prod_4_reaction =  data[1112 + i*11250].split()[0] 
				HCN_prod_4_flux = float(data[1112 + i*11250].split()[1]) 
				HCN_prod_4.append((HCN_prod_4_reaction, HCN_prod_4_flux))
				HCN_prod_5_reaction =  data[1113 + i*11250].split()[0] 
				HCN_prod_5_flux = float(data[1113 + i*11250].split()[1]) 
				HCN_prod_5.append((HCN_prod_5_reaction, HCN_prod_5_flux))
				HCN_prod_6_reaction =  data[1114 + i*11250].split()[0] 
				HCN_prod_6_flux = float(data[1114 + i*11250].split()[1]) 
				HCN_prod_6.append((HCN_prod_6_reaction, HCN_prod_6_flux))
				HCN_prod_7_reaction =  data[1115 + i*11250].split()[0] 
				HCN_prod_7_flux = float(data[1115 + i*11250].split()[1]) 
				HCN_prod_7.append((HCN_prod_7_reaction, HCN_prod_7_flux))
				HCN_prod_8_reaction =  data[1116 + i*11250].split()[0] 
				HCN_prod_8_flux = float(data[1116 + i*11250].split()[1]) 
				HCN_prod_8.append((HCN_prod_8_reaction, HCN_prod_8_flux))
				HCN_prod_9_reaction =  data[1117 + i*11250].split()[0] 
				HCN_prod_9_flux = float(data[1117 + i*11250].split()[1]) 
				HCN_prod_9.append((HCN_prod_9_reaction, HCN_prod_9_flux))
				HCN_prod_10_reaction =  data[1118 + i*11250].split()[0] 
				HCN_prod_10_flux = float(data[1118 + i*11250].split()[1]) 
				HCN_prod_10.append((HCN_prod_10_reaction, HCN_prod_10_flux))
				HCN_tot_flux = float(data[1119 + i*11250].split()[7]) 
				HCN_dest_tot.append(('destruction_tot', HCN_tot_flux))
				HCN_dest_1_reaction =  data[1120 + i*11250].split()[0] 
				HCN_dest_1_flux = abs(float(data[1120 + i*11250].split()[1])) 
				HCN_dest_1.append((HCN_dest_1_reaction, HCN_dest_1_flux))
				HCN_dest_2_reaction =  data[1121 + i*11250].split()[0] 
				HCN_dest_2_flux = abs(float(data[1121 + i*11250].split()[1])) 
				HCN_dest_2.append((HCN_dest_2_reaction, HCN_dest_2_flux))
				HCN_dest_3_reaction =  data[1122 + i*11250].split()[0] 
				HCN_dest_3_flux = abs(float(data[1122 + i*11250].split()[1])) 
				HCN_dest_3.append((HCN_dest_3_reaction, HCN_dest_3_flux))
				HCN_dest_4_reaction =  data[1123 + i*11250].split()[0] 
				HCN_dest_4_flux = abs(float(data[1123 + i*11250].split()[1])) 
				HCN_dest_4.append((HCN_dest_4_reaction, HCN_dest_4_flux))
				HCN_dest_5_reaction =  data[1124 + i*11250].split()[0] 
				HCN_dest_5_flux = abs(float(data[1124 + i*11250].split()[1])) 
				HCN_dest_5.append((HCN_dest_5_reaction, HCN_dest_5_flux))
				HCN_dest_6_reaction =  data[1125 + i*11250].split()[0] 
				HCN_dest_6_flux = abs(float(data[1125 + i*11250].split()[1])) 
				HCN_dest_6.append((HCN_dest_6_reaction, HCN_dest_6_flux))
				HCN_dest_7_reaction =  data[1126 + i*11250].split()[0] 
				HCN_dest_7_flux = abs(float(data[1126 + i*11250].split()[1])) 
				HCN_dest_7.append((HCN_dest_7_reaction, HCN_dest_7_flux))
				HCN_dest_8_reaction =  data[1127 + i*11250].split()[0] 
				HCN_dest_8_flux = abs(float(data[1127 + i*11250].split()[1])) 
				HCN_dest_8.append((HCN_dest_8_reaction, HCN_dest_8_flux))
				HCN_dest_9_reaction =  data[1128 + i*11250].split()[0] 
				HCN_dest_9_flux = abs(float(data[1128 + i*11250].split()[1])) 
				HCN_dest_9.append((HCN_dest_9_reaction, HCN_dest_9_flux))
				HCN_dest_10_reaction =  data[1129 + i*11250].split()[0] 
				HCN_dest_10_flux = abs(float(data[1129 + i*11250].split()[1])) 
				HCN_dest_10.append((HCN_dest_10_reaction, HCN_dest_10_flux))

			total_lists = {'CN_prod_tot': CN_prod_tot, 'HCN_prod_tot': HCN_prod_tot, 'CN_dest_tot': CN_dest_tot, 'HCN_dest_tot': HCN_dest_tot}

	#########production
		

			production = {'CN_production': {'CN_prod_1': CN_prod_1, 'CN_prod_2': CN_prod_2, 'CN_prod_3': CN_prod_3, 'CN_prod_4': CN_prod_4, 'CN_prod_5': CN_prod_5, 'CN_prod_6': CN_prod_6, 'CN_prod_7': CN_prod_7, 'CN_prod_8': CN_prod_8, 'CN_prod_9': CN_prod_9, 'CN_prod_10': CN_prod_10}, 'HCN_production': {'HCN_prod_1': HCN_prod_1, 'HCN_prod_2': HCN_prod_2, 'HCN_prod_3': HCN_prod_3, 'HCN_prod_4': HCN_prod_4, 'HCN_prod_5': HCN_prod_5, 'HCN_prod_6': HCN_prod_6, 'HCN_prod_7': HCN_prod_7, 'HCN_prod_8': HCN_prod_8, 'HCN_prod_9': HCN_prod_9, 'HCN_prod_10': HCN_prod_10}}

			destruction = {'CN_destruction': {'CN_dest_1': CN_dest_1, 'CN_dest_2': CN_dest_2, 'CN_dest_3': CN_dest_3, 'CN_dest_4': CN_dest_4, 'CN_dest_5': CN_dest_5, 'CN_dest_6': CN_dest_6, 'CN_dest_7': CN_dest_7, 'CN_dest_8': CN_dest_8, 'CN_dest_9': CN_dest_9, 'CN_dest_10': CN_dest_10}, 'HCN_destruction': {'HCN_dest_1': HCN_dest_1, 'HCN_dest_2': HCN_dest_2, 'HCN_dest_3': HCN_dest_3, 'HCN_dest_4': HCN_dest_4, 'HCN_dest_5': HCN_dest_5, 'HCN_dest_6': HCN_dest_6, 'HCN_dest_7': HCN_dest_7, 'HCN_dest_8': HCN_dest_8, 'HCN_dest_9': HCN_dest_9, 'HCN_dest_10': HCN_dest_10}}

			for molecule in ['CN','HCN']:

				reaction_lists = []
				for i in range(1,4):
					for reaction in transpone_matrix(production[f'{molecule}_production'][f'{molecule}_prod_{i}'])[0]:
						if reaction not in reaction_lists:
							reaction_lists.append(reaction)
				
				production_shorter = {'CN_production_shorter': {'CN_2135': [], 'CN_347': [], 'CN_6546': [], 'CN_2025': [], 'CN_2024': [], 'CN_5305': [], 'CN_6560': [], 'CN_264': [], 'CN_350': [], 'CN_402': [], 'CN_2055': [], 'CN_6810': [], 'CN_3466': []}, 'HCN_production_shorter': {'HCN_5046': [], 'HCN_4535': [], 'HCN_2043': [], 'HCN_5047': [], 'HCN_6811': [], 'HCN_6821': [], 'HCN_2052': [], 'HCN_1984': [], 'HCN_6871': [], 'HCN_5174': []}}
				for reaction in reaction_lists: 
					for i in range(len(CN_prod_1)):
						if production[f'{molecule}_production'][f'{molecule}_prod_1'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_1'][i][1])
						elif production[f'{molecule}_production'][f'{molecule}_prod_2'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_2'][i][1])
						elif production[f'{molecule}_production'][f'{molecule}_prod_3'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_3'][i][1])
						elif production[f'{molecule}_production'][f'{molecule}_prod_4'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_4'][i][1])
						elif production[f'{molecule}_production'][f'{molecule}_prod_5'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_5'][i][1])
						elif production[f'{molecule}_production'][f'{molecule}_prod_6'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_6'][i][1])
						elif production[f'{molecule}_production'][f'{molecule}_prod_7'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_7'][i][1])
						elif production[f'{molecule}_production'][f'{molecule}_prod_8'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_8'][i][1])
						elif production[f'{molecule}_production'][f'{molecule}_prod_9'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_9'][i][1])
						elif production[f'{molecule}_production'][f'{molecule}_prod_10'][i][0] == reaction:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append(production[f'{molecule}_production'][f'{molecule}_prod_10'][i][1])
						else:
							production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'].append((total_lists[f'{molecule}_prod_tot'][i][1])/100)

				total_lists_prod_trans = transpone_matrix(total_lists[f'{molecule}_prod_tot'])

				time_prod = time[:-1]
				lists = [time_prod[1:], total_lists_prod_trans[1]]

				for reaction in reaction_lists:
					lists.append(production_shorter[f'{molecule}_production_shorter'][f'{molecule}_{reaction}'])

				reaction_lists_for_method = limit_lists(lists) #ratio at 10^4, ratio at 10^5, integral [0, 5*10^4]

				methods = ['ratio at 1e4 yr', 'ratio at 1e5 yr', 'ratio of integrals between 0 and 5e4 yr']
				
				for j in range(len(reaction_lists_for_method)):
					for i in range(len(reaction_lists_for_method[j])):
						reaction = reaction_lists[reaction_lists_for_method[j][i][1]-2]
						if reaction not in writed_reactions_prod:
							write_to_file('production_'+molecule+'_'+reaction+'_'+methods[j], density, G0, reaction_lists_for_method[j][i][0])
							writed_reactions_prod.append(reaction)
						else:
							append_to_file('production_'+molecule+'_'+reaction+'_'+methods[j], density, G0, reaction_lists_for_method[j][i][0])

				#shorter_lists = [lists[0], lists[1]]
				#for mol_list in lists[2:]:
				#	if sum(mol_list) > 0.1*sum(lists[1]):
				#		shorter_lists.append(mol_list)

				#log_lists = make_log_lists(shorter_lists) 

				

				#for CN_list in log_lists[2:]:
				#	if max(CN_list) > min(log_lists[1])-1:
				#		shorter_lists.append(CN_list)
			

				#make_picture(log_lists, point, reaction_lists, f'{molecule}_production')

	####destruction
			
				reaction_lists = []
				for i in range(1,4):
					for reaction in transpone_matrix(destruction[f'{molecule}_destruction'][f'{molecule}_dest_{i}'])[0]:
						if reaction not in reaction_lists:
							reaction_lists.append(reaction)

				destruction_shorter = {'CN_destruction_shorter': {'CN_2116': [], 'CN_2027': [], 'CN_4535': [], 'CN_312': [], 'CN_2024': [], 'CN_5305': [], 'CN_6560': [], 'CN_264': [], 'CN_350': [], 'CN_402': [], 'CN_2055': [], 'CN_6810': [], 'CN_898': [], 'CN_4760': [], 'CN_4889': [], 'CN_211': []}, 'HCN_destruction_shorter': {'HCN_347': [], 'HCN_589': [], 'HCN_1745': [], 'HCN_3014': [], 'HCN_4759': [], 'HCN_2793': []}}
				
				for reaction in reaction_lists: 
						for i in range(len(CN_prod_1)):
							if destruction[f'{molecule}_destruction'][f'{molecule}_dest_1'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_1'][i][1])
							elif destruction[f'{molecule}_destruction'][f'{molecule}_dest_2'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_2'][i][1])
							elif destruction[f'{molecule}_destruction'][f'{molecule}_dest_3'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_3'][i][1])
							elif destruction[f'{molecule}_destruction'][f'{molecule}_dest_4'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_4'][i][1])
							elif destruction[f'{molecule}_destruction'][f'{molecule}_dest_5'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_5'][i][1])
							elif destruction[f'{molecule}_destruction'][f'{molecule}_dest_6'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_6'][i][1])
							elif destruction[f'{molecule}_destruction'][f'{molecule}_dest_7'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_7'][i][1])
							elif destruction[f'{molecule}_destruction'][f'{molecule}_dest_8'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_8'][i][1])
							elif destruction[f'{molecule}_destruction'][f'{molecule}_dest_9'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_9'][i][1])
							elif destruction[f'{molecule}_destruction'][f'{molecule}_dest_10'][i][0] == reaction:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append(destruction[f'{molecule}_destruction'][f'{molecule}_dest_10'][i][1])
							else:
								destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'].append((total_lists[f'{molecule}_dest_tot'][i][1])/100)
				

				total_lists_dest_trans = transpone_matrix(total_lists[f'{molecule}_dest_tot'])

				time_dest = time[:-1]
				lists = [time_dest[1:], total_lists_dest_trans[1]]

				for reaction in reaction_lists:
					lists.append(destruction_shorter[f'{molecule}_destruction_shorter'][f'{molecule}_{reaction}'])

				reaction_lists_for_method = limit_lists(lists) #ratio at 10^4, ratio at 10^5, integral [0, 5*10^4]

				methods = ['ratio at 1e4 yr', 'ratio at 1e5 yr', 'ratio of integrals between 0 and 5e4 yr']

				for j in range(len(reaction_lists_for_method)):
						for i in range(len(reaction_lists_for_method[j])):
							reaction = reaction_lists[reaction_lists_for_method[j][i][1]-2]
							if reaction not in writed_reactions_dest:
								write_to_file('destruction_'+molecule+'_'+reaction+'_'+methods[j], density, G0, reaction_lists_for_method[j][i][0])
								writed_reactions_dest.append(reaction)
							else:
								append_to_file('destruction_'+molecule+'_'+reaction+'_'+methods[j], density, G0, reaction_lists_for_method[j][i][0])
					
				
				#for mol_list in lists[2:]:
				#	if sum(mol_list) > 0.1*sum(lists[1]):
				#		shorter_lists.append(mol_list)

				#log_lists = make_log_lists(shorter_lists) 

				

				#for CN_list in log_lists[2:]:
				#	if max(CN_list) > min(log_lists[1])-1:
				#		shorter_lists.append(CN_list)
			

				#make_picture(log_lists, point, reaction_lists, f'{molecule}_destruction')

if __name__ == '__main__':
	main()
