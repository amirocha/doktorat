"""Cutting spectra to equal lenght of (-100, 100) km/s velocity range"""

def read_file(filename):
	file1=open(str(filename)+'.txt','r')
	lines=file1.readlines()
	file1.close()

	return lines

def cut_data(lines):
	x1=[] 
	y1=[]  #flux
	for i in range(len(lines)):  #velocities
		line=lines[i]
		elem=line.split() 
		elem2=elem[0]
		elem3=float(elem2)
		elem4=float(elem[1])
		if elem3<13 and elem3>5:
			x1.append(elem3)
			y1.append(elem4)

	return x1, y1

def write_file(filename, x1, y1):

	file2=open(str(filename)+'_cut.txt','w')
	b=[]
	for i in range(len(x1)):
		a=str(x1[i]) 
		c=str(y1[i]) 
		b.append(a)
		b.append(' ')
		b.append(c)
		b.append('\n')
	file2.writelines(b)
	file2.close()

def main():
	for i in [1,2,3,4,5,6,9,10,12]: #SMM
		filename = 'serpens_cn10_smm'+str(i)
		lines = read_file(filename)
		x, y = cut_data(lines)
		write_file(filename, x, y)

if __name__ == '__main__':
	main()
   

 
   
 
