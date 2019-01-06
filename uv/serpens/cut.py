"""Cutting spectra to equal lenght of (-100, 100) km/s velocity range"""

file1=open('smm1_co65.txt','r')
lines=file1.readlines()
file1.close()

x1=[] 
y1=[]  #flux
for i in range(len(lines)):  #velocities
   line=lines[i]
   elem=line.split() 
   elem2=elem[0]
   elem3=float(elem2)
   elem4=float(elem[1])
   if elem3<100 and elem3>-100:
      x1.append(elem3)
      y1.append(elem4)


file2=open('smm1_co65_cut.txt','w')
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
   

 
   
 
