"""Removes additional filds in CO maps"""
"""Cuts out area delta>180"""

file1=open('serpens_13co65_int.txt','r')
lines=file1.readlines()
file1.close()

cut=[] 
for i in range(5,len(lines)):  #skip header
   line=lines[i]
   elem=float(line.split()[2])
   if elem < 180.: 
   	cut.append(line)

fileend=open('serpens_13co65_cut.txt','w')
fileend.writelines(cut)
fileend.close()

