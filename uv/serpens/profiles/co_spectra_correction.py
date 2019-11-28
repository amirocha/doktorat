"""Correction for V_lsr in CO 6-5 line"""



for source in ['smm1', 'smm5', 'smm9', 'smm10', 'pos1', 'pos4']:

	file1=open('serpens_co65_'+source+'.txt','r')
	lines=file1.readlines()
	file1.close()

	velocity=[] 
	flux=[]
	for i in range(len(lines)):  
		vel=float(lines[i].split()[0])
		vel+=8.5
		velocity.append(vel)
		flux.append(lines[i].split()[1])
	   
	file2=open('serpens_co65_'+source+'_cut.txt','w')
	new_lines=[]
	for i in range(len(flux)):
		new_lines.append(str(velocity[i]))
		new_lines.append(' ')
		new_lines.append(str(flux[i]))
		new_lines.append('\n')
	file2.writelines(new_lines)
	file2.close()
   

for source in ['smm2', 'smm3', 'smm4', 'smm6', 'smm12', 'pos2', 'pos3', 'pos5']:

	file1=open('serpens_co65_'+source+'.txt','r')
	lines=file1.readlines()
	file1.close()

	velocity=[] 
	flux=[]
	for i in range(len(lines)):  
		vel=float(lines[i].split()[0])
		vel+=8.5
		velocity.append(vel)
		flux.append(lines[i].split()[1])
	   
	file2=open('serpens_co65_'+source+'_cut.txt','w')
	new_lines=[]
	for i in range(len(flux)):
		new_lines.append(str(velocity[i]))
		new_lines.append(' ')
		new_lines.append(str(flux[i]))
		new_lines.append('\n')
	file2.writelines(new_lines)
	file2.close()
   
   
 
