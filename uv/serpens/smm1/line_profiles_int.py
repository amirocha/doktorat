"""profile lines integration (rectangle method)"""


def read_data(pos,mol,i):
	x=[]
	y=[]
	file1=open('./spectra/smm' + str(pos) + '_' + mol + '_' + str(i) + '_offset.txt','r') 
	lines=file1.readlines()
	for i in range(len(lines)):  
		x.append(float(lines[i].split()[0]))
		y.append(float(lines[i].split()[1]))
	file1.close()
	return x,y



def integrate(x,y,mol,integrals):
	integral=0
	for i in range(len(x)-1):
		if x[i]>-50.9 and x[i]<4.8:  #CO6-5 SMM1: -50.9 4.8 (north), -50.1 12.9 (south)  HCN1-0: -4.8 1.1 (north)
			integral+=y[i]*(x[i+1]-x[i])
	integrals.append(integral)
	return integrals



def main():  #activate the rest of functions
	integrals=[]
	file2=open('fluxes_co65_N.txt','w')
	file2.write('Protostar   Molecule   Pixel number  Flux\n')
	pos = 1  #SMM1
#SMM1 CO6-5 South
#	for i in [1,2,9,10,11,18,19,20,21,28,29,30,37,38,39,46,47,48,55,56,57,58,63,64,65,66,67,73,74,75,76,77,84,85,86,92,93,94,95,96,102,103,104,109,110,111,112,113,114,115,116,119,120,121,122,123,124,128,129,130,131,132,138,139,140,145,146,147,148,149,150,151,158,159,160]: 

#SMM1 CO6-5 North
	for i in range(34):
		if i not in [0,1,4,9,10,15,20,25,26,30,31,34]:
			for mol in ['co65']:
				(x,y)=read_data(pos,mol,i)
				if mol != 'cn10':
					integrals=integrate(x,y,mol,integrals)
				else: 
					integratecn(x,y,integrals)
				file2.write("smm%s   %s   %s   %f\n" % (pos,mol,i,integrals[-1]))

	

if __name__ == '__main__': #sth with files importing?
	main()




			
		



