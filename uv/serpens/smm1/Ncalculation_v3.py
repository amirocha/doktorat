"""Outflow parameters calculation (based on Yildiz et al. 2015)"""

import math as m
from decimal import Decimal

molecules = ['hcn10', 'co65', 'cn10']


k=1.38065*10**(-23) #Boltzmann's constant in J/K
m_H = 1.008*1.660538921*(10**(-27)) #mass of hydrogen atom [kg]
M_sun = 1.9884*(10**30) #Sun mass [kg]
beta = 1937 #[(GHz^2 K km)^-1]
mi_H2 = 2.8

def readdata(mol):
	data=[]
	file1=open('fluxes_'+mol+'.txt','r') #fluxes and positions 
	lines=file1.readlines()
	for i in range(len(lines)):
		if mol == lines[i].split()[1]:
			data.append(lines[i].split()[3])			
	file1.close()

	return data

def calculate_mass(flux, mol, D, M_outflow, T_ex=100):
	
	freq={'co65': 691.4730763, 'hcn10': 88.6316022, 'cn10': 113.1686723} # line frequency [GHz]
	Eu={'co65': 116.16, 'hcn10': 4.25, 'cn10': 5.43}  # Energy of the upper level per kB [K]
	g={'co65': 13.0, 'hcn10': 3.0, 'cn10': 3.0} # g_up statistical weight []
	A={'co65': 2.137e-05, 'hcn10': 2.407E-05, 'cn10': 1.182E-05} #Einstein coefficient	[s^-1]

	pixel_size={'co65': 4.5, 'hcn10': 14.65, 'cn10': 14.65} 
	relative_abudance={'co65': 1.2*(10**(4)), 'hcn10': 10**(7), 'cn10': 1*10**7} #H_2/mol relative abudances: CO6-5 (Yildiz et al. 2012), HCN1-0 (Hirota et al. 1998), CN1-0 (Hily-Blant et al. 2013)

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

def main():  #activate the rest of functions

	D = 436*3.086*pow(10,18) #distance to the source [cm]
	T_ex=7. #exitation temperature in Kelvins: 75K for CO (Yildiz et al. 2015), 7K for HCN, CS (Tafalla+2010)
	
	for mol in molecules:
		fluxes = readdata(mol)
		M_outflow = 0.
		for i in range(len(fluxes)):
			M_outflow=calculate_mass(fluxes[i], mol, D, M_outflow, T_ex)
				
		print(M_outflow)

if __name__ == '__main__': 
	main()
