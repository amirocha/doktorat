"""Finds the highest value in integrated flux list"""

file1=open('smm34_co65_blue_map.txt','r')
lines=file1.readlines()
file1.close()

fluxes=[]
for i in range(len(lines)):
   line=lines[i]
   flux=float(line.split()[3])
   fluxes.append(flux)  #list of fluxes
   
maximum=max(fluxes)
index = fluxes.index(maximum)  #index of the maximum flux
ra=lines[index].split()[1]  #position of the maximum flux
dec=lines[index].split()[2]


print(maximum, ra, dec)



