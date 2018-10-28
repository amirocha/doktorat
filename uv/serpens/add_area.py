#-*-coding: utf-8-*-
'''Adding areas of different CN 1-0 lines'''
import math as m


file1=open('serpens_cn10_1_int.txt','r')
lines=file1.readlines()
file1.close()

added=[] 
for i in range(5,len(lines)):  #read the first area
   line=lines[i]
   elem=line.split() 
   elem2=float(elem[3])
   added.append(elem2)



file2=open('serpens_cn10_2_int.txt','r')
lines2=file2.readlines()
file2.close()


added2=[]
for i in range(5,len(lines2)):  #read the second area
   line=lines2[i]
   elem=line.split() 
   elem2=float(elem[3])
   added2.append(elem2)
  

file3=open('serpens_cn10_3_int.txt','r')
lines=file3.readlines()
file3.close()

added3=[]
for i in range(5,len(lines)):  #read the third area
   line=lines[i]
   elem=line.split() 
   elem2=float(elem[3])
   added3.append(elem2)

file4=open('serpens_cn10_4_int.txt','r')
lines=file4.readlines()
file4.close()

added4=[]
for i in range(5,len(lines)):  #read the fourth area
   line=lines[i]
   elem=line.split() 
   elem2=float(elem[3])
   added4.append(elem2)


file5=open('serpens_cn10_5_int.txt','r')
lines=file5.readlines()
file5.close()

added5=[]
for i in range(5,len(lines)):  #read the fifth area
   line=lines[i]
   elem=line.split() 
   elem2=float(elem[3])
   added5.append(elem2)


column4=[]
for i in range(len(added)):  #add all lists
   elem=added4[i]+added[i]+added2[i]+added3[i]+added5[i]
   column4.append(elem)


column1=[] 
for i in range(5,len(lines)):  #rewrite the first column
   line=lines[i]
   elem=line.split() 
   elem2=elem[0]
   elem3=' '+elem2
   column1.append(elem3)

column2=[] 
for i in range(5,len(lines)):  #rewrite the second column
   line=lines[i]
   elem=line.split() 
   elem2=elem[1]
   elem3='    '+elem2
   column2.append(elem3)

column3=[] 
for i in range(5,len(lines)):  #rewrite the third column
   line=lines[i]
   elem=line.split() 
   elem2=elem[2]
   elem3='     '+elem2+'  '
   column3.append(elem3)

fileend=open('cn10_area.txt','w')

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

