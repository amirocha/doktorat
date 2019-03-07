"""Outflow parameters calculation (based on Yildiz et al. 2015)"""

import math as m
from decimal import Decimal

regions=['N','S']
molecules=['co65']
itteration_per_region={'S': 8, 'N': 5} #CO6-5: S-74, N-27 //HCN1-0 S-8, N-5
radius = {'N':22.36, 'S': 82.46} #ouflow size in arcsec  CO6-5 SMM1 North: 22.36'' //CO6-5 SMM1 South: 82.46'' //HCN1-0 SMM1 North: 31.62'' //HCN1-0 SMM1 South: 60.83''

k=1.38065*10**(-23) #Boltzmann's constant in J/K
m_H = 1.008*1.660538921*(10**(-27)) #mass of hydrogen atom [kg]
M_sun = 1.9884*10**30 #Sun mass [kg]
L_sun = 3.827*(10**26) #Solar luminosity [W]

def readdata(mol,region):
	data=[]
	file1=open('fluxes_'+mol+'_'+region+'.txt','r') #fluxes and positions 
	lines=file1.readlines()
	for i in range(len(lines)):
		if mol == lines[i].split()[1]:
			data.append([lines[i].split()[0], mol, lines[i].split()[2], lines[i].split()[3], '\n'])			
	file1.close()
	return data

def calculate_mass(data, mol, D, M_outflow, T_ex=100):
	     
	freq={'co65': 691473.0763, 'hcn10': 88630.416} # line frequency [MHz]
	Eu={'co65': 33.18543390620297, 'hcn10': 4.25358399778}  # Energy of the upper level per kB [K]
	lamda={'co65': 433.5562269526936, 'hcn10': 3382.50085614} #line wavelenght [mikrons]
	g={'co65': 13.0, 'hcn10': 3.0} # g_up statistical weight []
	A={'co65': 1.3653727183397027e-05, 'hcn10': 5.34650660346e-07} #Einstein coefficient	[s^-1]

	pixel_size={'co65': 4.5, 'hcn10': 14.65} 
	relative_abudance={'co65': 1.2*(10**(4)), 'hcn10': 10**(9)} #H_2/mol relative abudances: CO6-5 (Yildiz et al. 2012), HCN1-0 (Hirota et al. 1998)

	N=(1937*((freq[mol]/1000.)**2)*float(data[3]))/(A[mol])  #freq in GHz (Yildiz et al. 2015, eq. (1))
		
	N_g=N/g[mol] #column density devided by g (eq.1)
	# Total column density for all lines (eq. 2)
	N_tot = N_g * partition_function(mol, T_ex) * m.exp(Eu[mol]/T_ex)  
	print('%.2E' % Decimal(N_tot))
	M_out = 2.8*m_H*(pixel_size[mol]**2)*relative_abudance[mol]*N_tot #outflow mass [kg*arcsec^2*cm^-2] (eq.3)
	pixel_size_in_radians = pixel_size[mol]*((2*m.pi)/(360*60*60)) # arcsec -> rad
	pixel_size_in_cms = pixel_size_in_radians*D #rad -> cm
	pixel_size_in_AU = pixel_size_in_cms/14959787070000.
	S_in_cms = pixel_size_in_cms**2
	result=(1./M_sun)*2.8*m_H*S_in_cms*relative_abudance[mol]*N_tot #outflow mass [M_sun]
	return M_outflow+result #sum of all itterations
				
def partition_function(mol, T_ex):  #based on Rossi, Maciel, Benevides-Soares 1985
	a0={'co65':5.26251e-1, 'hcn10': 1.27223e+0}
	a1={'co65':1.43697e+0, 'hcn10': 3.28968e+0}
	a2={'co65':-5.6342e-1, 'hcn10': -1.22452e+0}
	a3={'co65':1.02007e-1, 'hcn10': 2.11961e-1}
	a4={'co65':-6.93012e-3, 'hcn10': -1.3954e-2}
	a5={'co65':6.94849e-2, 'hcn10': -2.15849e-1}
	a6={'co65':5.3743e+0, 'hcn10': 5.42514e+0}

	Z=T_ex/1000. #eq. 9
	lnQ = a0[mol]*m.log(Z)+(a1[mol]/2.)*Z+(a2[mol]/6.)*(Z**2)+(a3[mol]/12.)*(Z**3)+(a4[mol]/20.)*(Z**4)-(a5[mol]/Z)+a6[mol] #eq. 11
	Q=m.exp(lnQ)
	return Q

def calculate_force(R, M_outflow, V_max):
	Force=(V_max**2*M_outflow)/R
	return Force

def main():  #activate the rest of functions

	file2=open('Outflows_paramaters.txt','a') #append (in the file) 
	title=['Position    ', 'Molecule    ', 'Pixels number', '     M_outfllow [M_sun]', '      Mass loss [M_sun/yr]','     R [AU]', '       t_dyn [yr]', '     F_outflow [M_sun/yr km/s]\n']
	#file2.writelines(title)
	D = 260*3.086*(10**18) #distance to the source [cm]
	T_ex=75 #exitation temperature in Kelvins
	#T_ex for CO6-5: 75K (Yildiz et al. 2015) //HCN the same
	c=50. #inclination (Yildiz el al. 2015) SMM1: 50
	c_rad=m.radians(c) #inclination in radians
	results=[]	
	for mol in molecules:
		for reg in regions:
			R_arcsec=radius[reg] #ouflow size in arcsec  CO6-5 SMM1 North: 22.36'' //CO6-5 SMM1 South: 82.46'' //HCN1-0 SMM1 North: 31.62'' //HCN1-0 SMM1 South: 60.83''
			R_radians=R_arcsec*((2*m.pi)/(360*60*60)) # arcsec -> rad
			R_cm=R_radians*D #ouflow size in cm
			R_km=R_cm/100000. #ouflow size in km
			R_AU=R_cm/14959787070000. #ouflow size in AU
			R_AU_corr=R_AU/m.sin(c_rad) #corrected for inclination
			#print(m.sin(c_rad))
			R=R_km/m.sin(c_rad)  #R in km corrected for inclination 
			V_max = abs(-50.1) #outflow maximum velocity (greater integration limit) [km/s]
	
			data=readdata(mol, reg)
			M_outflow=0.
			for i in range(itteration_per_region[reg]):
			
				M_outflow=calculate_mass(data[i], mol, D, M_outflow, T_ex)
				
			t_dyn_s=R/V_max #dynamic time in sec
			t_dyn=t_dyn_s/(60*60*24*365.25) #dynamic time in yr 
				
			M_dot_s	= M_outflow/t_dyn_s #mass loss [M_sun/s]
			M_dot=M_outflow/t_dyn #mass loss [M_sun/yr]
			
			F_outflow_s=(c*M_outflow*(V_max)**2)/(R_km) #outflow force [M_sun/s*km/s]
			F_outflow=F_outflow_s/(60*60*24*365.25)  #outflow force [M_sun/yr*km/s]
			
			L_kin_watt=0.5*F_outflow_s*M_sun*V_max*1000. #kinetic luminosity [kg*m^2*s^-3]
			L_kin=L_kin_watt/L_sun #kinetic luminosity [L_sun]
			results.append((M_outflow, M_dot, R_AU_corr, t_dyn, F_outflow, i))
'''
	file2.write("%3s %7s %12s %24s %24s %14s %15s %25s\n" % (data[1][0]+" North",data[1][1],results[0][5]+1,'{:0.3e}'.format(results[0][0]), '{:0.3e}'.format(results[0][1]), int(results[0][2]), int(results[0][3]), '{:0.3e}'.format(results[0][4])))
	file2.write("%3s %7s %12s %24s %24s %14s %15s %25s\n" % (data[1][0]+" South",data[1][1],i+1,'{:0.3e}'.format(results[1][0]), '{:0.3e}'.format(results[1][1]), int(results[1][2]), int(results[1][3]), '{:0.3e}'.format(results[1][4])))
	file2.write("\n")
	file2.write("%3s %7s %12s %24s %24s %14s %15s %25s\n" % (data[1][0]+"Sum/Ave",data[1][1],results[0][5]+results[1][5],'{:0.3e}'.format(results[0][0]+results[1][0]), '{:0.3e}'.format((results[0][1]+results[1][1])/2.), int(results[0][2]+results[1][2]), int((results[0][3]+results[1][3])/2.), '{:0.3e}'.format((results[0][4]+results[1][4]))))
	file2.close()
'''
if __name__ == '__main__': 
	main()
