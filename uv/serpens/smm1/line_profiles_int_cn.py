"""profile lines integration (rectangle method)"""

freq0 = {'cn10': 113490.982, 'hcn10': 88631.602, 'c34s32': 144617.101, 'cs32': 146969.049, 'h13cn10': 86342.274, 'h13cn21': 172677.851}  
c=299792.458 #speed of light [km/s]

def read_data(pos,mol,i):
	x=[]
	y=[]
	file1=open('./spectra/smm' + str(pos) + '_' + mol + '_' + str(i) + '.txt','r') 
	lines=file1.readlines()
	for i in range(len(lines)):  
		x.append(float(lines[i].split()[0]))
		y.append(float(lines[i].split()[1]))
	file1.close()
	return x,y

def integratecn(x,y,integrals):  #poprawic na hyperfine splitting
	integral=0
	for i in range(len(x)-1):
		if x[i]>-70.2 and x[i]<-68.9:
			integral+=y[i]*(x[i+1]-x[i])
		if x[i]>13.9 and x[i]<17.1:
			integral+=y[i]*(x[i+1]-x[i])
		if x[i]>6.1 and x[i]<10.9:
			integral+=y[i]*(x[i+1]-x[i])
		if x[i]>-16.4 and x[i]<-13.7:
			integral+=y[i]*(x[i+1]-x[i])
		if x[i]>-40.4 and x[i]<-37.3:
			integral+=y[i]*(x[i+1]-x[i])
	integrals.append(integral)
	return integrals
	


def integrate(x,y,mol,integrals):
	integral=0
	for i in range(len(x)-1):
		if x[i]>-4.8 and x[i]<1.1:  #  Yildiz+2015: SMM1 blue: -10.5 6 //red: 10.5 31     old[CO6-5 SMM1: -50.9 4.8 (north), -50.1 12.9 (south)  HCN1-0: -4.8 1.1 (north)]
			integral+=y[i]*(x[i+1]-x[i])
	integrals.append(integral)
	return integrals


def main():  #activate the rest of functions
	integrals=[]
	file2=open('fluxes_cn10.txt','w')
	file2.write('Protostar   Molecule   Pixel number  Flux\n')
	pos = 1  #SMM1
#SMM1 CO6-5 South
#	for i in [1,2,9,10,11,18,19,20,21,28,29,30,37,38,39,46,47,48,55,56,57,58,63,64,65,66,67,73,74,75,76,77,84,85,86,92,93,94,95,96,102,103,104,109,110,111,112,113,114,115,116,119,120,121,122,123,124,128,129,130,131,132,138,139,140,145,146,147,148,149,150,151,158,159,160]: 

#SMM1 CO6-5 North
	for i in range(8):
		for mol in ['cn10']:
			(x,y)=read_data(pos,mol,i)
			if mol != 'cn10':
				integrals=integrate(x,y,mol,integrals)
			else: 
				integratecn(x,y,integrals)
			file2.write("smm%s   %s   %s   %f\n" % (pos,mol,i,integrals[-1]))

	

if __name__ == '__main__': #sth with files importing?
	main()




			
		



