'''Change pixel coordinates from JPEG picture to CLASS coordinates in arcsec'''

def read_data(file_name):

	file1 = open(file_name, 'r')
	data = file1.readlines()
	file1.close()

	return data

def write_to_file(data, file_end_name):

	file1 = open(file_end_name, 'w')
	file1.writelines(data)
	file1.close()

def change_coordinates(data):
	
	new_data = []
	i = 0
	for row in range(682):
		for col in range(191): 
			line=data[i].split()
			new_x = -84+col*2.1115
			new_y = -212+row*0.5013
			new_line = f'{col+row}\t{new_x}\t{new_y}\t{line[3]}\n'
			new_data.append(new_line)
			i += 1
	#new_data.join(\n)
	#print(new_data)
	return new_data

def main():
	file_name = 'serpens_dust.txt'
	file_end_name = 'serpens_dust_corr.txt'

	data = read_data(file_name)
	new_data = change_coordinates(data)
	write_to_file(new_data, file_end_name)
	

if __name__ == '__main__':
	main()
