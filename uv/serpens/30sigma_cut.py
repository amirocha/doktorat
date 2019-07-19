"""Cut intensity at 30 sigma"""


def read_data(filename):
	file = open(filename,'r')
	data = file.readlines()
	file.close()

	return data

def write_data(end_filename, data):
	file = open(end_filename,'w')
	file.writelines(data)
	file.close()

def sigma_cut(data, sigma, factor = 30):
	fluxes = []
	for line in data:
		if float(line.split()[3]) > factor * sigma:
			fluxes.append(line)
	return fluxes


def main():
	CN_data = read_data('serpens_cn10_int.txt') 
	HCN_data = read_data('serpens_hcn10_int.txt')
	sigma_CN = 8.106E-02 #rms level from CLASS channels 900 1150
	sigma_HCN = 0.239 #rms level from CLASS channels 1600 2000
	new_CN = sigma_cut(CN_data, sigma_CN, factor = 30)
	new_HCN = sigma_cut(HCN_data, sigma_HCN)
	write_data('serpens_cn10_int_30sigma.txt', new_CN)
	write_data('serpens_hcn10_int_30sigma.txt', new_HCN)
	
    
if __name__ == '__main__':
	main()
