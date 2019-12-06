'''Profiles/wings integration (rectangle method)'''

MOLECULES = {'cn10':5, 'hcn10':1}
SOURCES = {
	'smm3r' : {
		'cn10_total': {'comp1' : (-70.7, -69.4), 'comp2': (-41.2, -37.9), 'comp3' : (-16.6, -13.9), 'comp4' : (3.4, 9), 'comp5' : (13.7, 16.4)},
		'hcn10_total': {'comp1' : (-4.9, 15.2)},
	},
	'smm3b' : {
		'cn10_total': {'comp1' : (-70.7, -69.7), 'comp2': (-40.8, -37.9), 'comp3' : (-16.2, -14.1), 'comp4' : (5.3, 10), 'comp5' : (14.1, 16.4)},
		'hcn10_total': {'comp1' : (-1.5, 13.9)},
	},
	'smm4b' : {
		'cn10_total': {'comp1' : (-70.1, -69.), 'comp2': (-41.2, -37.5), 'comp3' : (-16.8, -13.1), 'comp4' : (3.2, 10.4), 'comp5' : (12.9, 17.2)},
		'hcn10_total': {'comp1' : (-6.2, 18.1)},
	}
}

def read_data(source, mol):
	x=[]
	y=[]
	file1=open('serpens_' + mol + '_' + str(source) + '.txt','r') 
	lines=file1.readlines()
	for i in range(len(lines)):  
		x.append(float(lines[i].split()[0]))
		y.append(float(lines[i].split()[1]))
	file1.close()
	return x,y

def integrate(x,y,limits):
	integral=0
	for i in range(len(x)-1):
		if x[i]>limits[0] and x[i]<limits[1]:  
			integral+=y[i]*(x[i]-x[i+1])
	return integral

def main():  
	integrals=[]
	file2=open('fluxes_profiles_Dionatos.txt','w')
	file2.write('Protostar   Molecule   Region   Flux\n')
	for mol,components in MOLECULES.items():
		for source in SOURCES.keys():
			x,y = read_data(source,mol)
			for region in ['total']:
				integral = 0
				for component in range(1,components+1):
					integral += integrate(x,y,SOURCES[source][f'{mol}_{region}'][f'comp{component}'])
				print(mol, region, integral)
				
				

				file2.write("%s   %s  %s  %f\n" % (source, mol, region, integral))

	

if __name__ == '__main__': 
	main()
