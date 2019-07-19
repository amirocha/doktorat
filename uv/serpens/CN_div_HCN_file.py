"""Make CN/HCN flux file"""

POSITIONS = [(-0.6, 1.4), (163.5, -142.7), (145.5, -78.80), (106.5, -123.3), (27, 77.8), (123, -75.2), (184.5, -11.3), (-22.95, 81), (37.5, 28.5), (142.5, -126.2), (-11., 33), (121., -121), (56, -112), (-54., 81), (143., -66)]  # SMM1 SMM2 SMM3 SMM4 SMM5 SMM6 SMM8 SMM9 SMM10 SMM12 pos1 pos2 pos3 pos4 pos5

def read_data(filename):
	file = open(filename,'r')
	data = file.readlines()
	file.close()

	return data

def write_data(end_filename, data):
	file = open(end_filename,'w')
	CN, HCN, div = data
	for i in range(len(data[0])):	
		file.write(f'{data[0][i]:10.3} {data[1][i]:10.3} {data[2][i]:10.3}\n')
	file.close()

def find_positions(data, pixel_size):
	fluxes = []
	for pos in POSITIONS:
		distance = 3000
		flux_temp = 0.
		for line in data:
			_, x, y, flux = line.split()
			point_distance = (float(x) - pos[0])**2 + (float(y) - pos[1])**2
			if point_distance < distance:
				distance = point_distance
				flux_temp = flux 
		fluxes.append(float(flux_temp))
	print(fluxes)
	return fluxes

def divide_fluxes(list1, list2): #lists of equal length
	divided_flux = []
	for i in range(len(list1)):
		divided = list1[i]/list2[i]
		divided_flux.append(divided)

	return divided_flux	

def main():
	CN_data = read_data('serpens_cn10_int.txt') 
	HCN_data = read_data('serpens_hcn10_int.txt')
	CN_list = find_positions(CN_data, pixel_size = 29.3)
	HCN_list = find_positions(HCN_data, pixel_size = 29.3)
	CN_div_HCN = divide_fluxes(CN_list, HCN_list)
	write_data('serpens_cn10_hcn10_fluxes.txt', (CN_list, HCN_list, CN_div_HCN))
	
	
if __name__ == '__main__':
	main()
