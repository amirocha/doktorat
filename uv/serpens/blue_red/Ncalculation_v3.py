"""Outflow parameters calculation (based on Yildiz et al. 2015)"""

import math as m
from decimal import Decimal

molecules = ['hcn10', 'cn10']
outflows = ['red', 'blue']
radius = {'hcn10': {'red':52.8, 'blue': 73.3}, 'cn10': {'red':58.6, 'blue':52.8}} #ouflow size in arcsec SMM1:{'hcn10': {'red':20.7, 'blue': 60.4}, 'cn10': {'red':46.1, 'blue':46}}
max_velocity = {'hcn10': 24.8, 'cn10': -69.7} #outflow maximum velocity (greater integration limit) [km/s]  //SMM1:{'hcn10': 15.9, 'cn10': -70}
v_source = 8.5 #V_LSR for SMM1/SMM9 [km/s]

k=1.38065*10**(-23) #Boltzmann's constant in J/K
m_H = 1.008*1.660538921*(10**(-27)) #mass of hydrogen atom [kg]
M_sun = 1.9884*(10**30) #Sun mass [kg]
beta = 1937 #[(GHz^2 K km)^-1]
mi_H2 = 2.8
L_sun = 3.827*(10**26) #Solar luminosity [W]

D = 436*3.086*pow(10,18) #distance to the source [cm]
T_ex=7. #exitation temperature in Kelvins: 75K for CO (Yildiz et al. 2015), 7K for HCN, CS (Tafalla+2010)

def readfluxes(mol, out):
	data=[]
	file1=open('fluxes_'+mol+'_'+out+'.txt','r') #fluxes and positions 
	lines=file1.readlines()
	for i in range(len(lines)):
		data.append(lines[i].split()[3])			
	file1.close()

	return data

def calculate_mass(flux, mol, M_outflow):
	
	freq={'co65': 691.4730763, 'hcn10': 88.6316022, 'cn10': 113.1686723} # line frequency [GHz]
	Eu={'co65': 116.16, 'hcn10': 4.25, 'cn10': 5.43}  # Energy of the upper level per kB [K]
	g={'co65': 13.0, 'hcn10': 3.0, 'cn10': 3.0} # g_up statistical weight []
	A={'co65': 2.137e-05, 'hcn10': 2.407E-05, 'cn10': 1.182E-05} #Einstein coefficient	[s^-1]

	pixel_size={'co65': 4.5, 'hcn10': 14.65, 'cn10': 14.65} 
	relative_abudance={'co65': 1.2*(10**(4)), 'hcn10': 10**(7), 'cn10': 1*10**6} #H_2/mol relative abudances: CO6-5 (Yildiz et al. 2012),       HCN (Tychoniec+2019)    ,CN - rząd wielkości więcej (RADEX)                //HCN1-0 (Hirota et al. 1998), CN1-0 (Hily-Blant et al. 2013)

	pixel_size_in_radians = m.radians(pixel_size[mol]/(3600)) # arcsec -> rad
	pixel_size_in_cms = pixel_size_in_radians*D #rad -> cm
	S_in_cms = pixel_size_in_cms**2
	

	N=(beta*pow(freq[mol],2)*float(flux))/(A[mol])  #freq in GHz (Yildiz et al. 2015, eq. (1)) #N_up
	N_g=N/g[mol] #column density devided by g (eq.1)
	
# Total column density for all lines (eq. 2)
	
	N_tot = N_g * partition_function(mol, T_ex) * m.exp(Eu[mol]/(T_ex))  
	
	M_outflow_pixel = (1./M_sun)*mi_H2*m_H*S_in_cms*relative_abudance[mol]*N_tot #outflow mass [M_sun]
	M_outflow += M_outflow_pixel

	return M_outflow 
				
def partition_function(mol, T_ex):  #linear approximation from JPL data
	if mol == 'hcn10': 
		return 1.4109992334108785*T_ex+1.008107178464627 
	if mol == 'co65': 
		return 0.36171900299102694*T_ex+0.33641974077767145 
	if mol == 'cn10': 
		return 2.206633355045973*T_ex+2.004509970089714
	if mol == 'cs32': 
		return 0.8507128038107898*T_ex+0.34633848454636507

def write_to_file(results):
	file2=open('Outflows_paramaters.txt','a') #append (in the file) 
	title='Molecule    Outflow         M_outfllow [M_sun]      Mass loss [M_sun/yr]     R [AU]       t_dyn [yr]     F_outflow [M_sun/yr km/s]        L_kin [L_sun]\n'
	#file2.write(title)
	for i in range(len(results)):
		file2.write("%7s %7s %12s %24s %24s %14s %15s %10s\n" % (results[i][6], results[i][7],'{:0.3e}'.format(results[i][0]), '{:0.3e}'.format(results[i][1]), int(results[i][2]), int(results[i][3]), '{:0.3e}'.format(results[i][4]), '{:0.3e}'.format(results[i][5])))

	file2.close()


def main():  #activate the rest of functions

	c=50. #inclination (Yildiz el al. 2015) SMM1: 50
	c_rad=m.radians(c) #inclination in radians
	results=[]
	for mol in molecules:
		for out in outflows:
			fluxes = readfluxes(mol, out)
			M_outflow = 0.
			M_dot = 0.
			F_outflow_s =0.

			R_arcsec=radius[mol][out] #ouflow size in arcsec  
			R_radians=R_arcsec*((2*m.pi)/(360*60*60)) # arcsec -> rad
			R_cm=R_radians*D #ouflow size in cm
			R_km=R_cm/100000. #ouflow size in km
			R_AU=R_cm/14959787070000. #ouflow size in AU
			R_AU_corr=R_AU/m.sin(c_rad) #corrected for inclination
			R=R_km/m.sin(c_rad)  #R in km corrected for inclination 
	
			t_dyn_s=R/abs(max_velocity[mol]) #dynamic time in sec
			t_dyn=t_dyn_s/(60*60*24*365.25) #dynamic time in yr 

			for i in range(len(fluxes)):
				M_outflow=calculate_mass(fluxes[i], mol, M_outflow)
				M_dot+=M_outflow/t_dyn #mass loss [M_sun/yr]
				F_outflow_s += (M_outflow * (abs(max_velocity[mol])-v_source)**2) / R_km #outflow force [M_sun/s*km/s]

			F_outflow = F_outflow_s*(60*60*24*365.25)  #outflow force [M_sun/yr*km/s]		
			M_dot_s	= M_outflow/t_dyn_s #mass loss [M_sun/s]
			M_dot=M_outflow/t_dyn #mass loss [M_sun/yr]
			
			#data = read_data(mol, out)
			L_kin_watt=0.5*F_outflow_s*M_sun*abs(max_velocity[mol])*1000**2 #kinetic luminosity [kg*m^2*s^-3]
			L_kin=L_kin_watt/L_sun #kinetic luminosity [L_sun]

			results.append((M_outflow, M_dot, R_AU_corr, t_dyn, F_outflow, L_kin, mol, out))
		
	write_to_file(results)
				

if __name__ == '__main__': 
	main()
