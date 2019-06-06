'''Change initial condition in KIDA code for output from dense dark cloud modelling'''

def read_data(filename):

	file_inp = open(filename,'r')
	data = file_inp.readlines()
	file_inp.close()

	return data

def write_data(data,filename):

	file_out = open(filename,'w')
	file_out.writelines(data)
	file_out.close()

	return data

def main():

	data = read_data('output.dat')
	data = data[1:]
	data[0] ='JSPACE = 0                \n'
	write_data(data,'cond_initial_kida.uva.2014.dat')

if __name__ == '__main__':
	main()
