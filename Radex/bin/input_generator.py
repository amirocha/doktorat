
TEMPERATURES = ['30', '75', '200']
H2_DENSITIES = ['1e4', '1e5', '1e6']
MOLECULES = ['hcn', 'cs', 'cn']
COLUMN_DENSITIES = ['1e6', '1e7', '1e8', '1e9', '1e10']


def generate_data(mol, temp, H2_dens, col_dens):
	freq = '50 500'
	par = '1'
	collidor = 'H2'
	CMB = '2.73'
	par2 = '1.0'
	par3 = '0'
	
	filename = f'{mol}{H2_dens}{temp}{col_dens}'
	data = f'{mol}.dat\n./output/{filename}.out\n{freq}\n{temp}\n{par}\n{collidor}\n{H2_dens}\n{CMB}\n{col_dens}\n{par2}\n{par3}'

	return data, filename


def write_to_file(data, filename):
	file1 = open('./input/'+filename, 'w')
	file1.write(data)
	file1.close()

def main():
	for mol in MOLECULES:
		for temp in TEMPERATURES:
			for H2_dens in H2_DENSITIES:
				for col_dens in COLUMN_DENSITIES:
					data, filename = generate_data(mol, temp, H2_dens, col_dens)
					write_to_file(data, filename+'.inp')

if __name__ == '__main__':
	main()
