'''Divide fluxes (total/wings)'''

def read_data():
	total = []
	wings = []
	file1 = open('fluxes_profiles_wings.txt','r') 
	lines = file1.readlines()
	for i in range(1,len(lines)): 
		if i%3 == 1: 
			total.append(float(lines[i].split()[3]))
		elif i%3 == 2:
			wing = float(lines[i].split()[3])
		else:
			wings.append(float(lines[i].split()[3])+wing)
	file1.close()
	return total, wings

def divide_lists_into_molecules(total, wings):
	cn_tot = []
	cn_wing = []
	hcn_tot = []
	hcn_wing = []
	cs_tot = []
	cs_wing = []
	co_tot = []
	co_wing = []
	h13cn_tot = []
	h13cn_wing = []
	c34s_tot = []
	h13cn21_tot = []
	for i in range(len(total)):
		if i<15:
			cn_tot.append(total[i])
			cn_wing.append(wings[i])
		elif i>=15 and i<30:
			hcn_tot.append(total[i])
			hcn_wing.append(wings[i])
		elif i>=30 and i<45:
			h13cn_tot.append(total[i])
			h13cn_wing.append(wings[i])
		elif i>=45 and i<60:
			h13cn21_tot.append(total[i])
		elif i>=60 and i<75:
			cs_tot.append(total[i])
			cs_wing.append(wings[i])
		elif i>=75 and i<90:
			c34s_tot.append(total[i])
		elif i>=90 and i<105:
			co_tot.append(total[i])
			co_wing.append(wings[i])
	return cn_tot, cn_wing, hcn_tot, hcn_wing, cs_tot, cs_wing, co_tot, co_wing, h13cn_tot, h13cn_wing, c34s_tot, h13cn21_tot
	
		
	

def main():  
	sources=['smm1', 'smm2', 'smm3', 'smm4', 'smm5', 'smm6', 'smm8', 'smm9', 'smm10', 'smm12', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']
	file2=open('fluxes_ratio.txt','w')
	file2.write('Protostar   Molecules   Flux_ratio\n')
	total, wings = read_data()
	cn_tot, cn_wing, hcn_tot, hcn_wing, cs_tot, cs_wing, co_tot, co_wing, h13cn_tot, h13cn_wing, c34s_tot, h13cn21_tot = divide_lists_into_molecules(total, wings)
	for i in range(len(sources)):
		file2.write("%s   %s   %f\n" % (sources[i], 'CN/HCN_tot', cn_tot[i]/hcn_tot[i]))
		file2.write("%s   %s   %f\n" % (sources[i], 'CN/HCN_wings', cn_wing[i]/hcn_wing[i]))
		if co_tot[i] != 0:
			file2.write("%s   %s   %f\n" % (sources[i], 'CS/CO_tot', cs_tot[i]/co_tot[i]))
			file2.write("%s   %s   %f\n" % (sources[i], 'CS/CO_wings', cs_wing[i]/co_wing[i]))
			file2.write("%s   %s   %f\n" % (sources[i], 'HCN/CO_tot', hcn_tot[i]/co_tot[i]))
			file2.write("%s   %s   %f\n" % (sources[i], 'HCN/CO_wings', hcn_wing[i]/co_wing[i]))
		file2.write("%s   %s   %f\n" % (sources[i], 'HCN/H13CN_tot', hcn_tot[i]/h13cn_tot[i]))
		if h13cn_wing[i] != 0:
			file2.write("%s   %s   %f\n" % (sources[i], 'HCN/H13CN_wings', hcn_wing[i]/h13cn_wing[i]))
		file2.write("%s   %s   %f\n" % (sources[i], 'CS/C34S_tot', cs_tot[i]/c34s_tot[i]))
		if h13cn21_tot[i] != 0:
			file2.write("%s   %s   %f\n" % (sources[i], 'H13CN10/H13CN21_tot', h13cn_tot[i]/h13cn21_tot[i]))
	file2.close()
	
	file3=open('Profiles_wings_ratio.txt','w')
	file3.write('Protostar   Molecule    Profile/wings \n')
	for i in range(len(sources)):
		file3.write("%s   %s   %f\n" % (sources[i], 'CN', cn_tot[i]/cn_wing[i]))
		file3.write("%s   %s   %f\n" % (sources[i], 'HCN', hcn_tot[i]/hcn_wing[i]))
		if co_tot[i] != 0:
			file3.write("%s   %s   %f\n" % (sources[i], 'CO', co_tot[i]/co_wing[i]))
		if h13cn_wing[i] != 0:
			file3.write("%s   %s   %f\n" % (sources[i], 'H13CN', h13cn_tot[i]/h13cn_wing[i]))
		file3.write("%s   %s   %f\n" % (sources[i], 'CS', cs_tot[i]/cs_wing[i]))
	file3.close()

	file3=open('Profiles_wings_percent.txt','w')
	file3.write('Protostar   Molecule    Profile/wings \n')
	for i in range(len(sources)):
		file3.write("%s   %s   %f\n" % (sources[i], 'CN', cn_wing[i]*100/cn_tot[i]))
		file3.write("%s   %s   %f\n" % (sources[i], 'HCN', 100*hcn_wing[i]/hcn_tot[i]))
		if co_tot[i] != 0:
			file3.write("%s   %s   %f\n" % (sources[i], 'CO', 100*co_wing[i]/co_tot[i]))
		if h13cn_wing[i] != 0:
			file3.write("%s   %s   %f\n" % (sources[i], 'H13CN', 100*h13cn_wing[i]/h13cn_tot[i]))
		file3.write("%s   %s   %f\n" % (sources[i], 'CS', 100*cs_wing[i]/cs_tot[i]))
	file3.close()

	

if __name__ == '__main__': 
	main()
