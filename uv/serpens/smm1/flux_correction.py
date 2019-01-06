"""Applies the flux correction for different base offsets"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import matplotlib.axes as ax

#SMM1 CO6-5 South
#positions = [i for i in [1,2,9,10,11,18,19,20,21,28,29,30,37,38,39,46,47,48,55,56,57,58,63,64,65,66,67,73,74,75,76,77,84,85,86,92,93,94,95,96,102,103,104,109,110,111,112,113,114,115,116,119,120,121,122,123,124,128,129,130,131,132,138,139,140,145,146,147,148,149,150,151,158,159,160]]

#SMM1 CO6-5 North
#positions = [i for i in range(34) if i not in [0,1,4,9,10,15,20,25,26,30,31,34]]
#molecules=['co65']

offsets=[]

#read data
#for pos in positions:
#	for mol in molecules:

file1=open('smm1_c18o65_ave_spec.txt','r')
lines=file1.readlines()
file1.close()


x1=[] 
for i in range(len(lines)):  #velocities
   line=lines[i]
   elem=line.split() 
   elem2=elem[0]
   x1.append(elem2)

y1=[]  #flux
for i in range(len(lines)):
   line=lines[i]
   elem=line.split()
   elem2=float(elem[1]) 
   y1.append(elem2)

#correct the base
y=sorted(y1) #sort fluxes
y=y[:-50] #cut out the line (the 50th highest values)
offset = sum(y)/len(y)   #arithmetic mean
offsets.append((offset))
y_offset = []
for elem in y1:
	new_elem = elem-offset
	y_offset.append(new_elem)

#save new data
file2=open('smm1_c18o65_offset.txt','w')
new_line=[]
for i in range(len(x1)):
	new_x=str(x1[i]) 
	new_y=str(y_offset[i]) 
	new_line.append(new_x)
	new_line.append(' ')
	new_line.append(new_y)
	new_line.append('\n')
file2.writelines(new_line)
file2.close()
"""
		
		#plot data
		fig = plt.figure(figsize = (9,7), dpi = 400)
		ax = fig.add_subplot(111)
		plt.ylabel("Flux", fontsize=12)
		#plt.title("CN (1-0)", fontsize=12)
		plt.xlabel("Velocity", fontsize=12)
		plt.tick_params(axis='x', which='both', top='off')
		plt.axhline(y=0., linewidth=0.5, color='r')
		#ax.margins(x=0.001)
		#ax.spines['bottom'].set_color('none')
		plt.plot(x1, y_offset, 'k-', linewidth=0.6, linestyle='steps')
		#plt.subplots_adjust(left=0.1, right=0.2)
		ax.set_ylim([-1.0, 0.5])

		plt.savefig('./plots/smm1_'+str(mol)+'_'+str(pos)+'.png')
		plt.clf()
		"""

print(offsets)

