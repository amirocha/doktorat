"""Removes additional filds in CO maps"""
"""Cuts out area delta>180"""

file1=open('serpens_co65_int.txt','r')
lines=file1.readlines()
file1.close()

cut=[] 
for i in range(5,len(lines)):  #skip header
   line=lines[i]
   dec=float(line.split()[2])
   ra=float(line.split()[1])
   if dec < 200. and dec > -240 and ra < 280 and ra > -100: 
   	cut.append(line)

fileend=open('serpens_co65_cut.txt','w')
fileend.writelines(cut)
fileend.close()

