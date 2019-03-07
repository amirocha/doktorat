"""Outflow parameters calculation (based on Yildiz et al. 2015)"""

import math as m
#import wdb
from decimal import Decimal

regions=['red','blue']
molecules=['hcn10']
flux = {'hcn10': {'red':62.087999999999994, 'blue': 28.5590744}, 'co65': {'red':2174.9757299999997, 'blue':1972.0615}} # from smm1_co65_fluxes.txt file
itteration = {'hcn10': 1, 'co65': 1} #CO6-5: S-74, N-23 //HCN1-0 S-8, N-5
radius = {'hcn10': {'red':31.62, 'blue': 60.83}, 'co65': {'red':92.2, 'blue':81.4}} #ouflow size in arcsec  CO6-5 SMM1 North: 22.36'' //CO6-5 SMM1 South: 82.46'' //HCN1-0 SMM1 North: 31.62'' //HCN1-0 SMM1 South: 60.83''

k=1.38065*10**(-23) #Boltzmann's constant in J/K
m_H = 1.008*1.660538921*(10**(-27)) #mass of hydrogen atom [kg]
M_sun = 1.9884*10**30 #Sun mass [kg]
L_sun = 3.827*(10**26) #Solar luminosity [W]
h=6.626068e-34  #Planck constant [J s]
c=3e10   # speed of light [cm/s]
mi_H2 = 2.72 #Walker-Smith+2014

def readdata(mol,region):
	data=[]
	file1=open('fluxes_'+mol+'_'+region+'.txt','r') #fluxes and positions 
	lines=file1.readlines()
	for i in range(len(lines)):
		if mol == lines[i].split()[1]:
			data.append([lines[i].split()[0], mol, lines[i].split()[2], lines[i].split()[3], '\n'])			
	file1.close()

	return data

def calculate_mass(data, mol, reg, D, M_outflow):

	T_ex={'co65': 75, 'hcn10': 9.375} #exitation temperature in Kelvins
	#T_ex for CO6-5: 75K (Yildiz et al. 2015) //HCN the same     
	freq={'co65': 691473.0763, 'hcn10': 88630.416} # line frequency [MHz]
	Eu={'co65': 33.18543390620297, 'hcn10': 4.25358399778}  # Energy of the upper level per kB [K]
	lamda={'co65': 433.5562269526936, 'hcn10': 3382.50085614} #line wavelenght [mikrons]
	g={'co65': 13.0, 'hcn10': 3.0} # g_up statistical weight []
	logI={'co65': -2.8193, 'hcn10': -2.9588} # Base 10 logarithm of the integrated intensity in units of nm^2 MHz at 300 K (from JPL database)
	El={'co65': 57.6704, 'hcn10': 0.} #[cm^-1]
	pixel_size={'co65': 4.5, 'hcn10': 14.65} #in arcsec
	relative_abundance={'co65': 1.2*(10**(4)), 'hcn10': 10**(9)} #H_2/mol relative abudances: CO6-5 (Yildiz et al. 2012), HCN1-0 (Hirota et al. 1998)
	Eup=El[mol]+freq[mol]*1000000./c #from Agata's code
	#A=(10**(-2.9588))*(freq[mol]**2)*(partition_function_v2(mol, T_ex[mol])*(1/g[mol])*(((m.exp(-(0.*h*c)/(k*T_ex[mol])))-(m.exp(-(Eup*h*c)/(k*T_ex[mol]))))**(-1))*2.7964e-16)  #from Agata's code
	#A=(10.**(logI[mol]))*(freq[mol]**2)*(partition_function(mol, T_ex)/g[mol])*((8*m.pi)/(c**2*m.exp(-El[mol]*h*c/(k*T_ex))-m.exp(-Eup*h*c/(k*T_ex))))
	A={'co65':6.126e-06, 'hcn10':2.407E-05} #from LAMDA database 
	#wdb.set_trace()
	#print(A_test,A)
	#const=8*m.pi/c**2
	#print(const)
	N=(1937*pow((freq[mol]/1000.),2)*flux[mol][reg])/A[mol]  #freq in GHz (Yildiz et al. 2015, eq. (1))
	#print('%.2E' % Decimal(N))	
	N_g=N/g[mol] #column density devided by g (eq.1)
	
	# Total column density for all lines (eq. 2)
	N_tot = N_g * partition_function_v2(mol, T_ex[mol]) * m.exp((Eu[mol]*h*c)/(k*T_ex[mol]))  

	### Walker-Smith 2014 eq.1
	eps0 = 8.8541878e-12 #in F/m = [A^2*s^4/kg*m^3]
	mi_e = {'hcn10': 2.98, 'co65': 0.112}  # in D (debye) = [3.333564*10e-30 A*s*m] from (https://physics.nist.gov/PhysRefData/MolSpec/Triatomic/Html/Tables/HCN.html) or Walker-Smith 2014
	eta_MB = {'hcn10': 0.75/0.92, 'co65': 0.18/0.75}  # HCN from https://www.iram.fr/IRAMFR/ARN/jan95/node46.html
	T_0 = {'hcn10': 4.25, 'co65': 5.53}
	J = {'hcn10': 0, 'co65': 5}

	#N_tot = (3*eps0*(pow(k,2))*1000*T_ex[mol]*m.exp(((J[mol]+1)*(J[mol]+2)*T_0[mol])/(2*T_ex[mol]))*flux[mol][reg])/(h*pow(m.pi,2)*pow(mi_e[mol]*3.333564e-30,2)*pow(freq[mol]*1e6,2)*pow((J[mol]+1),2)*eta_MB[mol])  #in m^-2

	N_tot_cm = N_tot/10000.
	
	#print('%.2E' % Decimal(partition_function_v2(mol, T_ex[mol])))
	#M_out = 2.8*m_H*(pixel_size[mol]**2)*relative_abudance[mol]*N_tot #outflow mass [kg*arcsec^2*cm^-2] (eq.3)
	pixel_size_in_radians = pixel_size[mol]*((2*m.pi)/(360*60*60)) # arcsec -> rad
	pixel_size_in_cms = pixel_size_in_radians*D #rad -> cm
	pixel_size_in_AU = pixel_size_in_cms/14959787070000.
	S_in_cms = pixel_size_in_cms**2

	result=(1./M_sun)*2.8*m_H*S_in_cms*relative_abundance[mol]*N_tot #outflow mass [M_sun]
	#result = (pow(D,2)*pow(pixel_size_in_radians,2)*mi_H2*m_H*N_tot_cm*relative_abundance[mol])/(M_sun)   	### Walker-Smith 2014 eq.3
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

def partition_function_v2(mol, T_ex):  #linear approximation from LAMDA data
	if mol == 'hcn10': 
		return {9.375: 14.272, 37.5: 53.914, 75: 106.807}[T_ex]
	if mol == 'co65': 
		return {37.5: 13.897, 75: 27.455, 150: 54.581}[T_ex]

def calculate_force(R, M_outflow, V_max):
	Force=(V_max**2*M_outflow)/R
	return Force

def main():  #activate the rest of functions

	file2=open('Outflows_paramaters.txt','a') #append (in the file) 
	title=['Position    ', 'Molecule    ', 'Pixels number', '     M_outfllow [M_sun]', '      Mass loss [M_sun/yr]','     R [AU]', '       t_dyn [yr]', '     F_outflow [M_sun/yr km/s]\n']
	#file2.writelines(title)
	D = 260*3.086*(10**18) #distance to the source [cm]
	c=50. #inclination (Yildiz el al. 2015) SMM1: 50
	c_rad=m.radians(c) #inclination in radians
	results=[]	
	for mol in molecules:
		for reg in regions:
			R_arcsec=radius[mol][reg] #ouflow size in arcsec  CO6-5 SMM1 North: 22.36'' //CO6-5 SMM1 South: 82.46'' //HCN1-0 SMM1 North: 31.62'' //HCN1-0 SMM1 South: 60.83''
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
			for i in range(itteration[mol]):
			
				M_outflow=calculate_mass(data[i], mol, reg, D, M_outflow)
			print(M_outflow)
			t_dyn_s=R/V_max #dynamic time in sec
			t_dyn=t_dyn_s/(60*60*24*365.25) #dynamic time in yr 
				
			M_dot_s	= M_outflow/t_dyn_s #mass loss [M_sun/s]
			M_dot=M_outflow/t_dyn #mass loss [M_sun/yr]
			
			F_outflow_s=(c*M_outflow*(V_max)**2)/(R_km) #outflow force [M_sun/s*km/s]
			F_outflow=F_outflow_s/(60*60*24*365.25)  #outflow force [M_sun/yr*km/s]
			
			L_kin_watt=0.5*F_outflow_s*M_sun*V_max*1000. #kinetic luminosity [kg*m^2*s^-3]
			L_kin=L_kin_watt/L_sun #kinetic luminosity [L_sun]
			results.append((M_outflow, M_dot, R_AU_corr, t_dyn, F_outflow, i, reg))
			

	file2.write("%3s %7s %12s %24s %24s %14s %15s %25s\n" % (data[1][0]+" "+results[0][6],data[1][1],results[0][5]+1,'{:0.3e}'.format(results[0][0]), '{:0.3e}'.format(results[0][1]), int(results[0][2]), int(results[0][3]), '{:0.3e}'.format(results[0][4])))
	file2.write("%3s %7s %12s %24s %24s %14s %15s %25s\n" % (data[1][0]+" "+results[1][6],data[1][1],i+1,'{:0.3e}'.format(results[1][0]), '{:0.3e}'.format(results[1][1]), int(results[1][2]), int(results[1][3]), '{:0.3e}'.format(results[1][4])))
	file2.write("\n")
	file2.write("%3s %7s %12s %24s %24s %14s %15s %25s\n" % (data[1][0]+"Sum/Ave",data[1][1],results[0][5]+results[1][5],'{:0.3e}'.format(results[0][0]+results[1][0]), '{:0.3e}'.format((results[0][1]+results[1][1])/2.), int(results[0][2]+results[1][2]), int((results[0][3]+results[1][3])/2.), '{:0.3e}'.format((results[0][4]+results[1][4]))))
	file2.close()

if __name__ == '__main__': 
	main()
