"""Cuts out area of a map"""


source = 'smm9'
RA = -22.95 
DEC = 81

for mol in ['hcn10','cn10']:
	for colour in ['red','blue']:
		file1=open(source+'_'+mol+'_'+colour+'.txt','r')
		lines=file1.readlines()
		file1.close()

		cut=[] 
		for i in range(5,len(lines)):  #skip header
		   line=lines[i]
		   dec=float(line.split()[2])
		   ra=float(line.split()[1])
		   if dec > DEC-75 and dec < DEC+75 and ra > RA-75 and ra < RA+75: 
		   	cut.append(line)

		fileend=open(source+'_'+mol+'_'+colour+'_map.txt','w')
		fileend.writelines(cut)
		fileend.close()

	for colour in ['red','blue']:
		file1=open(source+'_'+mol+'_'+colour+'.txt','r')
		lines=file1.readlines()
		file1.close()

		cut=[] 
		for i in range(5,len(lines)):  #skip header
		   line=lines[i]
		   dec=float(line.split()[2])
		   ra=float(line.split()[1])
		   if dec > DEC-100 and dec < DEC+100 and ra > RA-100 and ra < RA+100:  
		   	cut.append(line)

		fileend=open(source+'_'+mol+'_'+colour+'_map_large.txt','w')
		fileend.writelines(cut)
		fileend.close()

