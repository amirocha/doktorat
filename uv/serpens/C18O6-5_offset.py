
file1=open('serpens_c18o65_int.txt','r')
lines=file1.readlines()
file1.close()

new_line=[] 
for i in range(5,len(lines)):  #skip header
   line=lines[i]
   elem=float(line.split()[3])
   new_elem=elem-0.18494858258760125
   new_line.append(line.split()[0])
   new_line.append(' ')
   new_line.append(line.split()[1])
   new_line.append(' ')
   new_line.append(line.split()[2])
   new_line.append(' ')
   new_line.append(str(new_elem))
   new_line.append('\n')

fileend=open('serpens_c18o65_offset.txt','w')
fileend.writelines(new_line)
fileend.close()

