#-*-coding: utf-8-*-
'''Dividing areas of CN 1-0 / HCN 1-0 lines'''
import math as m



file2=open('smm1_hcn10_red_map_large.txt','r')
lines2=file2.readlines()
file2.close()

file1=open('smm1_cn10_red_map_large.txt','r')
lines=file1.readlines()
file1.close()

cn10=[] 
hcn10=[]
for i in range(len(lines)):  #read the first area
	for j in range(len(lines2)):  #read the second area
		if lines2[j].split()[1] == lines[i].split()[1] and lines2[j].split()[2] == lines[i].split()[2]:  
			hcn10_line=(lines2[j].split()[0],lines2[j].split()[1],lines2[j].split()[2],float(lines2[j].split()[3]))
			cn10_line=(lines[i].split()[0],lines[i].split()[1],lines[i].split()[2],float(lines[i].split()[3]))
			hcn10.append(hcn10_line)
			cn10.append(cn10_line)



column4=[]
for i in range(len(cn10)):  #add all lists
   elem=cn10[i][3]/hcn10[i][3]
   column4.append(elem)

column1=[] 
for i in range(len(cn10)):  #rewrite the first column
   column1.append(i+1)

column2=[] 
for i in range(len(cn10)):  #rewrite the second column
   column2.append(cn10[i][1])

column3=[] 
for i in range(len(cn10)):  #rewrite the third column
   column3.append(cn10[i][2])


fileend=open('smm1_cn10_hcn10_divided_red_large.txt','w')

results=[]
for i in range(len(column1)):
  elem1=str(column1[i]) 
  results.append(elem1)
  results.append(' ')
  
  elem2=str(column2[i]) 
  results.append(elem2)
  results.append(' ')
  
  elem3=str(column3[i]) 
  results.append(elem3)
  results.append(' ')
  
  elem4=str(column4[i]) 
  results.append(elem4)
  results.append(' ')
  
  results.append('\n')
fileend.writelines(results)

