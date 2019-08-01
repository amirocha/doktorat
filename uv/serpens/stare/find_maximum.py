"""Finds the highest value in integrated flux list"""

SOURCES = ['smm1', 'smm2', 'smm3', 'smm4', 'smm5', 'smm6', 'smm8', 'smm9', 'smm10', 'smm12', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']
MOLECULES = ['cn10', 'hcn10', 'cs32', 'c34s32', 'h13cn10', 'h13cn21']

for source in SOURCES:
	for mol in MOLECULES:

		file1=open('serpens_'+mol+'_'+source+'.txt','r')
		lines=file1.readlines()
		file1.close()

		fluxes=[]
		for i in range(len(lines)):
   			line=lines[i]
   			flux=float(line.split()[3])
   			fluxes.append(flux)  #list of fluxes
   
		maximum=max(fluxes)
#index = fluxes.index(maximum)  #index of the maximum flux
#ra=lines[index].split()[1]  #position of the maximum flux
#dec=lines[index].split()[2]


		print(source, mol, maximum)



