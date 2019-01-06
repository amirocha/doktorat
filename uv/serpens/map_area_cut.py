"""Cuts out area of a map"""

file1=open('smm1_hcn10_blue.txt','r')
lines=file1.readlines()
file1.close()

cut=[] 
for i in range(5,len(lines)):  #skip header
   line=lines[i]
   dec=float(line.split()[2])
   ra=float(line.split()[1])
   if dec > -80 and dec < 80 and ra > -80 and ra < 80: 
   	cut.append(line)

fileend=open('smm1_hcn10_blue_map.txt','w')
fileend.writelines(cut)
fileend.close()

#SMM1 RA: -50 50, DEC: -100 50   -> Yildiz+2015 -80 80, -80 80
#SMM34 RA:  20.5 220.5 , DEC: -178.8 21.2 (Yildiz+2015)

