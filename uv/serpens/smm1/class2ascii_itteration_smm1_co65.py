'''Changes ranges and output files for class2ascii.class script'''

starting_position=(-7.35, -2.85, -0.85, 3.65)

class2ascii_content="file in ../../serpens_co65_conv \nset range {} {} {} {}\nfind /all\naverage /nocheck /weight equal\nsic output ../spectra/{}.txt\nfor i 1 to channels\n\tsay 'rx[i]' 'ry[i]' /format g16.8 g16.8\nnext\nsic output"

def generate_script(i):
	positions=calculate_positions(i)
	output_file='smm1_co65_'+str(i)
	create_file(output_file, positions)

def create_file(output_file, positions):
	file2=open('./scripts/class2ascii_'+output_file+'.class','w')
	file2.write(class2ascii_content.format(positions[0],positions[1],positions[2],positions[3],output_file))
	file2.close()
	

def main():
	for i in [1,2,9,10,11,18,19,20,21,28,29,30,37,38,39,46,47,48,55,56,57,58,63,64,65,66,67,73,74,75,76,77,84,85,86,92,93,94,95,96,102,103,104,109,110,111,112,113,114,115,116,119,120,121,122,123,124,128,129,130,131,132,138,139,140,145,146,147,148,149,150,151,158,159,160]: #change number of changes (depending on the outflow pixels size)
		generate_script(i) 

def calculate_positions(i):
	new_x1 = starting_position[0]+(i%9)*4.5  #watch out the signs!
	new_x2 = starting_position[1]+(i%9)*4.5
	new_y1 = starting_position[2]-(i//9)*4.5
	new_y2 = starting_position[3]-(i//9)*4.5
	return (new_x1, new_x2, new_y1, new_y2)

if __name__ == '__main__': 
	main()
   
