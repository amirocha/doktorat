"""Outflow parameters calculation (based on Yildiz et al. 2015)"""

import math as m
from decimal import Decimal

molecules = ['hcn10', 'cn10', 'cs32']


k=1.38065*10**(-23) #Boltzmann's constant in J/K
m_H = 1.008*1.660538921*(10**(-27)) #mass of hydrogen atom [kg]
M_sun = 1.9884*(10**30) #Sun mass [kg]
beta = 1937 #[(GHz^2 K km)^-1]
mi_H2 = 2.8

def readdata(mol):
	data=[]
	file1=open('./../SMM_fluxes','r') #fluxes 
	lines=file1.readlines()
	for i in range(len(lines)):
		line = lines[i].split()
		if line[1] == mol:
			data.append(line)			
	file1.close()

	return data

def calculate_mass(line, mol, D, T_ex=100):
	
	flux = line[2]
	freq={'co65': 691.4730763, 'hcn10': 88.6316022, 'cn10': 113.1686723, 'cs32': 146.9690287} # line frequency [GHz]
	Eu={'co65': 116.16, 'hcn10': 4.25, 'cn10': 5.43, 'cs32': 14.1}  # Energy of the upper level per kB [K]
	g={'co65': 13.0, 'hcn10': 3.0, 'cn10': 3.0, 'cs32': 7.0} # g_up statistical weight []
	A={'co65': 2.137e-05, 'hcn10': 2.407E-05, 'cn10': 1.182E-05, 'cs32': 6.071e-5} #Einstein coefficient	[s^-1]

	pixel_size={'co65': 4.5, 'hcn10': 14.65, 'cn10': 14.65, 'cs32': 8.3} 
	relative_abudance={'co65': 1.2*(10**(4)), 'hcn10': 10**(9), 'cn10': 6.1*10**10, 'cs32': 2*10**8} #H_2/mol relative abudances: CO6-5 (Yildiz et al. 2012), HCN1-0 (Hirota et al. 1998), CN1-0 (Hily-Blant et al. 2013), CS3-2 (Bergin&Langer 1997)

	pixel_size_in_radians = m.radians(pixel_size[mol]/(3600)) # arcsec -> rad
	pixel_size_in_cms = pixel_size_in_radians*D #rad -> cm
	S_in_cms = pixel_size_in_cms**2
	

	N=(beta*pow(freq[mol],2)*float(flux))/(A[mol])  #freq in GHz (Yildiz et al. 2015, eq. (1)) #N_up
	N_g=N/g[mol] #column density devided by g (eq.1)
	
# Total column density for all lines (eq. 2)
	
	N_tot = N_g * partition_function(mol, T_ex) * m.exp(Eu[mol]/(T_ex))  
	
	
	M_outflow = (1./M_sun)*mi_H2*m_H*S_in_cms*relative_abudance[mol]*N_tot #outflow mass [M_sun]
	

	return N, N_tot
				
def partition_function(mol, T_ex):  #linear approximation from JPL data
	if mol == 'hcn10': 
		return {9.375: 14.272, 37.5: 53.914, 75: 106.807}[T_ex]
	if mol == 'cs32': 
		return {9.375: 8.316, 37.5: 32.240, 75: 64.150}[T_ex]
	if mol == 'co65': 
		return {37.5: 13.897, 75: 27.455, 150: 54.581}[T_ex]
	if mol == 'cn10': 
		return {37.5: 84.7308, 75: 167.4335, 150: 332.9077}[T_ex]

def main():  #activate the rest of functions

	D = 436*3.086*pow(10,18) #distance to the source [cm]
	T_ex=75 #exitation temperature in Kelvins (Yildiz et al. 2015)
	
	for mol in molecules:
		fluxes = readdata(mol)
		for i in range(len(fluxes)):
			N, N_tot = calculate_mass(fluxes[i], mol, D, T_ex)
				
			print(fluxes[i][0], mol, '%.2E' % Decimal(N), '%.2E' % Decimal(N_tot))

if __name__ == '__main__': 
	main()
