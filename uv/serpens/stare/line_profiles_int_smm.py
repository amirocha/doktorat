"""profile lines integration (rectangle method)"""

'''
c=299792.458 #speed of light [km/s]

freq0 = {'cn10': 113490.982, 'hcn10': 88631.602, 'c34s32': 144617.101, 'cs32': 146969.049, 'h13cn10': 86342.274, 'h13cn21': 172677.851}  

positions=range(1,7)
positions.append(9)
positions.append(10)
positions.append(12)
molecules=['cn10','hcn10','c34s32','cs32','h13cn10','h13cn21']
'''

def read_data(pos,mol):
	x=[]
	y=[]
	file1=open('smm' + str(pos) + '_' + mol + '_3sigma.txt','r') 
	lines=file1.readlines()
	for i in range(len(lines)):  
		x.append(float(lines[i].split()[0]))
		y.append(float(lines[i].split()[1]))
	file1.close()
	return x,y

def find_peaks(n,x,y): #n - peaks number
	maxima_list=[]
	ascending=True
	for i in range(1,len(y)):
		if y[i]<y[i-1]:
			if ascending==True:
				maxima_list.append(y[i-1])
				ascending=False
		else:
			ascending=True

	peaks=[]
	for i in range(n):
		temp_max=max(maxima_list)
		peaks.append(temp_max)
		maxima_list.remove(temp_max)

	return [x[y.index(g)] for g in peaks]
	
'''
def integratecn(x,y,integrals):  #poprawic na hyperfine splitting
	index=1
	for peak_pos in find_peaks(3,x,y):
		integral=0
 		profile_start=x.index(peak_pos)+1
		profile_end=x.index(peak_pos)-1		
		while y[profile_start+1]<y[profile_start]:
			profile_start+=1
			if profile_start==len(x)-1:
				break
		while y[profile_end]>y[profile_end-1]:
			profile_end-=1
			if profile_start==1:
				break
		for i in range(profile_end, profile_start):
			integral+=y[i]*(x[i]-x[i+1])
		freq=freq0['hcn10']-((peak_pos*freq0['hcn10'])/c)
		integrals.append([index, integral, freq, peak_pos])
		index+=1
'''

def integrate(x,y,mol,integrals):
	integral=0
	for i in range(len(x)-1):
		if x[i]>1.4 and x[i]<14.4:
			integral+=y[i]*(x[i]-x[i+1])
	integrals.append(integral)

'''
def velocity2freq(x,mol):  #Doppler effect
	for ni in x:
		freq=freq0[mol]-((ni*freq0[mol])/c)
	return freq
'''

def main():  #activate the rest of functions
	integrals=[]
	file2=open('fluxes.txt','w')
	file2.write('Protostar Molecule Flux\n')
	for pos in [1]:
		for mol in ['co65']:
			(x,y)=read_data(pos,mol)
			if mol != 'cn10':
				integrate(x,y,mol,integrals)
			else: 
				integratecn(x,y,integrals)
			for i in range(len(integrals)):
				file2.write("smm%s %s %f\n" % (pos,mol,integrals[i]))
			integrals=[]
	
	

if __name__ == '__main__': #sth with files importing?
	main()




			
		



