"""profile lines integration (rectangle method)"""


def read_data(pos,mol):
	x=[]
	y=[]
	file1=open('serpens_' + mol + '_pos' + str(pos) + '.txt','r') 
	lines=file1.readlines()
	for i in range(len(lines)):  
		x.append(float(lines[i].split()[0]))
		y.append(float(lines[i].split()[1]))
	file1.close()
	return x,y



def integrate(x,y,mol,integrals):
	integral=0
	for i in range(len(x)-1):
		if x[i]>-1.7 and x[i]<15.2:  #  Yildiz+2015: SMM1 blue: -10.5 6 //red: 10.5 31     old[CO6-5 SMM1: -50.9 4.8 (north), -50.1 12.9 (south)  HCN1-0: -4.8 1.1 (north)]
			integral+=y[i]*(x[i]-x[i+1])
	integrals.append(integral)
	return integrals

def integratecn(x,y,integrals):  #poprawic na hyperfine splitting
	integral=0
	for i in range(len(x)-1):
		if x[i]>-71.9 and x[i]<-68.6:
			integral+=y[i]*(x[i]-x[i+1])
		if x[i]>-41.6 and x[i]<-38.1:
			integral+=y[i]*(x[i]-x[i+1])
		if x[i]>-17 and x[i]<-12.9:
			integral+=y[i]*(x[i]-x[i+1])
		if x[i]>2.4 and x[i]<18.1:
			integral+=y[i]*(x[i]-x[i+1])
	integrals.append(integral)
	return integrals
#base on 3sigma level: outflow2 - HCN -1 23 // CN -71 -68,5 -42,2 -35,8 -16,6 -12,5 2,6 19,5  ////outflow5 - HCN  1,7 15,2 //CN -71,9 -68,6 -41,6 -38,1 -17 -12,9 2,4 18,1

def main():  #activate the rest of functions
	integrals=[]
	file2=open('fluxes_regtangular_method.txt','a')
	file2.write('Protostar   Molecule  Flux\n')
	positions = [5]  #SMM1
	for mol in ['hcn10', 'cn10']:
		for pos in positions:
			(x,y)=read_data(pos,mol)
			if mol != 'cn10':
				integrals=integrate(x,y,mol,integrals)
			else: 
				integrals=integratecn(x,y,integrals)
			file2.write("outflow%s   %s   %f\n" % (pos,mol,integrals[-1]))

	

if __name__ == '__main__': #sth with files importing?
	main()




			
		



