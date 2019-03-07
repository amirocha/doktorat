"""Add fluxes for blue and red outflows separely"""

file1=open('smm1_co65_blue_map_small.txt','r')
lines=file1.readlines()
file1.close()


sigma = 1.343E-02  #CO6-5: 2.475E-02  // HCN1-0: 1.343E-02
flux = 0 
for i in range(len(lines)): 
   line=lines[i]
   elem=float(line.split()[3])
   if elem > 3*sigma: 
      flux += elem

fileend=open('smm1_co65_fluxes.txt','a')
output = 'v2_small blue ' + str(flux) 
fileend.writelines(output)
fileend.close()
