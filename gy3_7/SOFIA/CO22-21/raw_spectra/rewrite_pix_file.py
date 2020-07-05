'''Rewrite pix spectra to 2-column file'''


file_in=open('pix9-8.txt','r')
lines=file_in.readlines()
file_in.close()

out_line=[]
for i in range(6,len(lines)):  #skip header
	elem1=lines[i].split()[0]
	elem2=lines[i].split()[1]
	if elem2 != 'nan':
		out_line.append(elem1)
		out_line.append(' ')
		out_line.append(elem2)
		out_line.append('\n')


file_out=open('../pix9-8.txt','w')
file_out.writelines(out_line)
