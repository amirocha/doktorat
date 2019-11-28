"""Finds the highest value in integrated flux list"""

SOURCES = ['smm1', 'smm2', 'smm3', 'smm4', 'smm5', 'smm6', 'smm8', 'smm9', 'smm10', 'smm12', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']
MOLECULES = ['hcn10', 'cn10', 'cs32', 'c34s32', 'h13cn10']


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

file2 = open('T_max.txt','w')

for source in SOURCES:
	for mol in MOLECULES:

		file1=open('serpens_'+mol+'_'+source+'.txt','r')
		lines=file1.readlines()
		file1.close()

		fluxes=[]
		velocities=[]
		for i in range(len(lines)):
			line=lines[i]
			flux=float(line.split()[1])
			vel=float(line.split()[0])
			fluxes.append(flux)  #list of fluxes
			velocities.append(vel)
		maximum=max(fluxes)
		index = fluxes.index(maximum)  #index of the maximum flux
		#ra=lines[index].split()[1]  #position of the maximum flux
		#dec=lines[index].split()[2]


		print(source, mol, maximum)
		file2.write("%s   %s   %f\n" % (source, mol, maximum))

file2.close()
		
'''find velocities of components
		if mol=='hcn10':
			peaks = find_peaks(3,velocities,fluxes)
			print(peaks)
		elif mol=='cn10':
			peaks = find_peaks(5,velocities,fluxes)
			print(peaks)
'''
		



