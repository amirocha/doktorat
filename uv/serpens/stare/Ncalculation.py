"""Outflow parameters calculation (based on Yildiz et al. 2015)"""

import math as m

k=1.38065*10**(-23) #Boltzmann's constant in J/K
m_H = 1.008*1.660538921*(10**(-27)) #mass of hydrogen atom [kg]

def readdata(mol):
	data=[]
	file1=open('fluxes.txt','r') #fluxes and positions 
	lines=file1.readlines()
	for i in range(len(lines)):
		if mol == lines[i].split()[1]:
			data.append([lines[i].split()[0], mol, lines[i].split()[2], '\n'])			
	file1.close()
	return data

def calculate_parameters(data, mol, R, results, T_ex=100):
	freq={'co65': 691473.0763, 'cn10': 1} # line frequency [MHz]
	Eu={'co65': 33.18543390620297}  # Energy of the upper level per kB [K]
	lamda={'co65': 433.5562269526936} #line wavelenght [mikrons]
	g={'co65': 13.0} # g_up statistical weight []
	A={'co65': 1.3653727183397027e-05} #Einstein coefficient	[s^-1]

	pixel_size={'co65': 4.5} 
	relative_abudance={'co65': 1.2*(10**(4))} #H_2/mol relative abudances: CO6-5 (Yildiz et al. 2012)

	N=[]
	N_g=[]
	N_tot=[]
	M_outflow=[]
	for line in data:
		N_elem=(1937*((freq[mol]/1000)**2)*float(line[2]))/(A[mol])  #freq in GHz (Yildiz et al. 2015, eq. (1))
		N.append(N_elem)				 
	
		N_g_elem=N_elem/g[mol] #column density devided by g (eq.1)
		N_g.append(N_g_elem)
	# Total column density for all lines (eq. 2)
		N_tot_elem = N_g_elem * partition_function(mol, T_ex) * m.exp(Eu[mol]/T_ex)  
		N_tot.append(N_tot_elem)


		M_outflow_elem = 2.8*m_H*(pixel_size[mol]**2)*relative_abudance[mol]*N_tot_elem #[kg*arcsec^2*cm^-2]
		pixel_size_in_radians = pixel_size[mol]*((2*m.pi)/(360*360)) # arcsec -> rad
		pixel_size_in_cms = pixel_size_in_radians*R #rad -> cm
		S_in_cms = pixel_size_in_cms**2
		M_outflow_elem =(1./(1.9884*10**30))*2.8*m_H*S_in_cms*relative_abudance[mol]*N_tot_elem #[M_sun]
		M_outflow.append(M_outflow_elem)
	
		subresults=[]
        	subresults.append(pixel_size_in_cms)
		subresults.append(M_outflow)
		subresults.append('\n')
	        results.append(subresults)
	return results
				
def partition_function(mol, T_ex):  #based on Rossi, Maciel, Benevides-Soares 1985
	a0={'co65':5.26251e-1}
	a1={'co65':1.43697e+0}
	a2={'co65':-5.6342e-1}
	a3={'co65':1.02007e-1}
	a4={'co65':-6.93012e-3}
	a5={'co65':6.94849e-2}
	a6={'co65':5.3743e+0}

	Z=T_ex/1000. #eq. 9
	lnQ = a0[mol]*m.log(Z)+(a1[mol]/2.)*Z+(a2[mol]/6.)*(Z**2)+(a3[mol]/12.)*(Z**3)+(a4[mol]/20.)*(Z**4)-(a5[mol]/Z)+a6[mol] #eq. 11
	Q=m.exp(lnQ)
	print Q
	return Q

def main():  #activate the rest of functions

	file2=open('Outflows_paramaters.txt','a') #append (in the file) 
	title=['Position    ', 'Molecule    ', 'Freq   ', '        Flux    ', '     N\n']
	file2.writelines(title)
	file2.close()
	molecules=['co65','cn10']
	R = 260*3.086*(10**18) #distance to the source [cm]
	T_ex=150 #exitation temperature in Kelvins
	#T_ex for CO6-5: 75K (Yildiz et al. 2015)
	results=[]
	for mol in molecules:
		data=readdata(mol)
		results=calculate_parameters(data, mol, R, results, T_ex)
		print(results)
	#file2.write("%3s %14s %15s %10s %18s \n" % (results[0],results[1],results[2],results[3],results[4]))
	
if __name__ == '__main__': #sth with files importing?
	main()
