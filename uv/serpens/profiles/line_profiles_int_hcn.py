"""profile lines integration (rectangle method)"""


def read_data(pos,mol,i):
	x=[]
	y=[]
	file1=open('serpens_smm' + str(pos) + '_' + mol + '.txt','r') 
	lines=file1.readlines()
	for i in range(len(lines)):  
		x.append(float(lines[i].split()[0]))
		y.append(float(lines[i].split()[1]))
	file1.close()
	return x,y



def integrate(x,y,mol,integrals):
	integral=0
	for i in range(len(x)-1):
		if x[i]>-4.8 and x[i]<1.1:  #  Yildiz+2015: SMM1 blue: -10.5 6 //red: 10.5 31     old[CO6-5 SMM1: -50.9 4.8 (north), -50.1 12.9 (south)  HCN1-0: -4.8 1.1 (north)]
			integral+=y[i]*(x[i+1]-x[i])
	integrals.append(integral)
	return integrals



def main():  #activate the rest of functions
	integrals=[]
	file2=open('fluxes_hcn10.txt','w')
	file2.write('Protostar   Molecule  Flux   N_up\n')
	pos = [1,2,3,4,5,6,8,9,10,12]  #SMM1
	for mol in ['hcn10', 'cn10', 'h13cn10', 'h13cn21', 'cs32', 'c34s32']:
		(x,y)=read_data(pos,mol,i)
		if mol != 'cn10':
			integrals=integrate(x,y,mol,integrals)
		else: 
			integrals=integratecn(x,y,integrals)
		N_up = calculate_N(integrals)
		file2.write("smm%s   %s   %s   %f\n" % (pos,mol,integrals[-1]), )

	

if __name__ == '__main__': #sth with files importing?
	main()




			
		



