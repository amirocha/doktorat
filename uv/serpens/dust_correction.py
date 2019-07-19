"""Changing flux units from RGB colour to Jy/arcsec^2"""

file1=open('serpens_dust.txt','r')
lines=file1.readlines()
file1.close()

factor = 0.001874609
lp1=[]
x1=[] 
y1=[]  #positions
z1=[]  #flux
for i in range(len(lines)):  #velocities
   line=lines[i].split() 
   lp = line[0]
   x = line[1]
   y = line[2]
   z = float(line[3]) * factor
   lp1.append(lp)
   x1.append(x)
   y1.append(y)
   z1.append(z)


file2=open('serpens_dust_corr.txt','w')
new_file=[]
for i in range(len(x1)):
  lp2=str(lp1[i]) 
  x2=str(x1[i]) 
  y2=str(y1[i]) 
  z2=str(z1[i])
  new_file.append(lp2)
  new_file.append(' ')
  new_file.append(x2)
  new_file.append(' ')
  new_file.append(y2)
  new_file.append(' ')
  new_file.append(z2)
  new_file.append('\n')
file2.writelines(new_file)
file2.close()
   

 
   
 
