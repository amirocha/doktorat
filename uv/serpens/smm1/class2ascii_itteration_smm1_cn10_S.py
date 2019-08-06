'''Changes ranges and output files for class2ascii.class script'''

starting_position=(-14.5, 13.3, -12.5, 15.3)

class2ascii_content="file in ../../serpens_cn10_conv \nset range {} {} {} {}\nfind /all\naverage /nocheck /weight equal\nsic output ../spectra/{}.txt\nfor i 1 to channels\n\tsay 'rx[i]' 'ry[i]' /format g16.8 g16.8\nnext\nsic output"

def generate_script(i):
	positions=calculate_positions(i)
	output_file='smm1_cn10_'+str(i)
	create_file(output_file, positions)

def create_file(output_file, positions):
	file2=open('./scripts/class2ascii_'+output_file+'.class','w')
	file2.write(class2ascii_content.format(positions[0],positions[1],positions[2],positions[3],output_file))
	file2.close()

def calculate_positions(i):
	new_x1 = starting_position[0]-(i%2)*14.65  #watch out the signs!
	new_x2 = starting_position[1]-(i%2)*14.65
	new_y1 = starting_position[2]-(i//2)*14.65
	new_y2 = starting_position[3]-(i//2)*14.65
	return (new_x1, new_x2, new_y1, new_y2)

def main():
	for i in range(8): #change number of changes (depending on the outflow pixels size)
			generate_script(i) 

if __name__ == '__main__': 
	main()
   
