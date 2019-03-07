#-*-coding: utf-8-*-
'''Calculating ratios of different CN 1-0 lines (components)'''
import math as m
import numpy as np
from copy import copy

def find_maxima(n,CN_fluxes):
   maxima_indexes=[]
   list_copy=copy(CN_fluxes)
   for i in range(n):
      maximum=max(list_copy)
      index = list_copy.index(maximum)  #index of the maximum flux
      maxima_indexes.append(index)
      list_copy[index]=0
   return maxima_indexes

def prepare_list(maxima_indexes, list_to_prep):
   prepared_list=[]
   for index in maxima_indexes:
      prepared_list.append(list_to_prep[index])
   return prepared_list

def calculate_mean(ratio_list):
   ratio_sum=0.
   for i in ratio_list:
      ratio_sum+=i
   return ratio_sum/len(ratio_list)

def calculate_std(ratio_list, mean):
   std=0.
   for i in ratio_list:
      std+=m.pow(i-mean,2)
   return m.sqrt(std/len(ratio_list))

def calculate_median(ratio_list):
   sorted_list=sorted(ratio_list) #sorted - doesn't change the original list
   if len(sorted_list)%2==0: 
      return (sorted_list[int(len(sorted_list)/2)]+sorted_list[int(len(sorted_list)/2-1)])/2
   return sorted_list[int(len(sorted_list)/2)]


file1=open('serpens_cn10_1_int.txt','r')
lines=file1.readlines()
file1.close()


comp1=[]  #components intesity ratio normalised to the highest peak - component no.3 [based on mean values of ech component]
for i in range(5,len(lines)):  #read the first area
   line=lines[i]
   elem=line.split() 
   elem2=float(elem[3])
   comp1.append(elem2)



file2=open('serpens_cn10_2_int.txt','r')
lines2=file2.readlines()
file2.close()


comp2=[]
for i in range(5,len(lines2)):  #read the second area
   line=lines2[i]
   elem=line.split() 
   elem2=float(elem[3])
   comp2.append(elem2)
  

file3=open('serpens_cn10_3_int.txt','r')
lines=file3.readlines()
file3.close()

comp3=[]
for i in range(5,len(lines)):  #read the third area
   line=lines[i]
   elem=line.split() 
   elem2=float(elem[3])
   comp3.append(elem2)

file4=open('serpens_cn10_4_int.txt','r')
lines=file4.readlines()
file4.close()

comp4=[]
for i in range(5,len(lines)):  #read the fourth area
   line=lines[i]
   elem=line.split() 
   elem2=float(elem[3])
   comp4.append(elem2)


file5=open('serpens_cn10_5_int.txt','r')
lines=file5.readlines()
file5.close()

comp5=[]
for i in range(5,len(lines)):  #read the fifth area
   line=lines[i]
   elem=line.split() 
   elem2=float(elem[3])
   comp5.append(elem2)

file6=open('serpens_cn10_int.txt','r')
lines=file6.readlines()
file6.close()

fluxes=[]
for i in range(5,len(lines)):  #read the total fluxes (all components added)
   line=lines[i]
   elem=line.split() 
   elem2=float(elem[3])
   fluxes.append(elem2)

maxima_list=find_maxima(10, fluxes)   #choose 10 the highest values of total fluxes and cut the other components' lists
comp1=prepare_list(maxima_list, comp1)
comp2=prepare_list(maxima_list, comp2)
comp3=prepare_list(maxima_list, comp3)
comp4=prepare_list(maxima_list, comp4)
comp5=prepare_list(maxima_list, comp5)


ratio1=[]
for i in range(len(comp4)):  #calculate ratio 
   elem=comp1[i]/comp3[i]
   ratio1.append(elem)

ratio2=[]
for i in range(len(comp4)): 
   elem=comp2[i]/comp3[i]
   ratio2.append(elem)

ratio3=[]
for i in range(len(comp4)):  
   elem=comp4[i]/comp3[i]
   ratio3.append(elem)

ratio4=[]
for i in range(len(comp4)):  
   elem=comp5[i]/comp3[i]
   ratio4.append(elem)

#calculate mean and standard deviation for every ratios

means_list=[]
stds_list=[]
medians_list=[]



for ratio in [ratio1, ratio2, ratio3, ratio4]:
   print(ratio)
   mean=calculate_mean(ratio)
   means_list.append(mean)
   median=calculate_median(ratio)
   medians_list.append(median)
   std=calculate_std(ratio, mean)
   stds_list.append(std)
 



fileend=open('CN_components_ratio.txt','a')

fileend.write("%3s %16s %16s %16s \n" % ("Component 1/3","Component 2/3","Component 4/3","Component 5/3"))
fileend.write("%3s \n" % ("Mean"))
fileend.write("%3s %16s %16s %16s \n" % tuple(means_list))
fileend.write("%3s \n" % ("Median"))
fileend.write("%3s %16s %16s %16s \n" % tuple(medians_list))
fileend.write("%3s \n" % ("Standard devation"))
fileend.write("%3s %16s %16s %16s \n" % tuple(stds_list))
for i in range(len(ratio1)):
   fileend.write("%3f %16f %16f %16f \n" % (ratio1[i],ratio2[i],ratio3[i],ratio4[i]))
