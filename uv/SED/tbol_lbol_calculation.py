'''
***************************************************************************************
 Program for calculating Tbol and Lbol with 2 methods:
 1) Trapezodial sumation of all the data collected
 2) Linear interpolation and trapezodial sumation of these new
 generated data. For the interpolation we use the program: "loglev.pro"

 The program generates the SEDs plots (saved in the folder: "plots")

 Modification;10-May-2011
***************************************************************************************
'''
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math as m
import numpy as np
from scipy.interpolate import interp1d
import scipy.integrate as integrate


from matplotlib import rc
rc('font',**{'family':'serif','serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})

  
def read_data(filename):
	file1 = open(filename,'r')
	data = file1.readlines()
	file1.close()

	return data
  
obj='Ser SMM1'
file_name='smm1.inp'   
file_name_newpoints='smm1_newpoints.txt'
  
output_file_name_sed='sed_'+str(obj)+'.eps'
output_file_name_view='view_'+str(obj)+'.eps'
output_file_name_values='values_'+str(obj)+'.txt'
  
dist=429. 
   
 
#-------------------------------------------------------
sou=obj  #strpos(file,"-frec_fl_1.1.txt")
#sou=strpos(file,"-frec_fl.txt")
#  source=strmid(file, 0, sou)

minii=1.0                     #for the interpolation, keep it always 1
mini=1.0

temp=str(mini)
tm=temp.find(".0000")
#mimm=STRTRIM(strmid(temp, 0, tm),2)  #usuwa spacje
#print(mimm)

#  file_out='values'+mimm+'.txt'
#  print, ;file_out

#-------------------------------------------------------


file1=read_data(file_name)   #wczytuje plik smm1 [dl. fali [mikrony] i flux [Jy]
file2=read_data(file_name_newpoints)   #wczytuje pliki z nowymi punktami
  
wave_lenghts = []
fluxes =[]

newpoints_wavelenghts=[]
newpoints_fluxes=[]


for i in range(len(file1)): 
	line=file1[i]
	wave_lenghts.append(float(line.split()[0]))
	fluxes.append(float(line.split()[1]))
  
for i in range(len(file2)): 
	line=file2[i]
	newpoints_wavelenghts.append(float(line.split()[0]))
	newpoints_fluxes.append(float(line.split()[1]))

all_points_wavelenghts=wave_lenghts+newpoints_wavelenghts
all_points_fluxes=fluxes+newpoints_fluxes



w=wave_lenghts #kolumna dlugosci
s=fluxes #kolumna flux
num=len(w) 

c=2.9979e14 #in microns
L_sun = 3.86e26 #W


newpoints_freq=[(c/wave) for wave in newpoints_wavelenghts]


def sort_points(list_to_sort, other_list):
	if len(list_to_sort) != len(other_list):
		raise 
	merged_list = [(list_to_sort[i], other_list[i]) for i in range(len(list_to_sort))]
	sorted_list = sorted(merged_list, key=lambda x: x[0])
	return [elem[0] for elem in sorted_list], [elem[1] for elem in sorted_list]

all_points_wavelenghts, all_points_fluxes = sort_points(all_points_wavelenghts, all_points_fluxes)
all_points_freq=[(c/wave) for wave in all_points_wavelenghts]

print(all_points_freq)

w_submm=[]
s_submm=[]
integral=0.
tbol=0.
for i in range(num-1):
	integral+=1e-26*s[i]*(abs((c/w[i+1])-(c/w[i]))) # calka pod wykresem 
	if w[i] > 349.:
		w_submm.append(w[i])
		s_submm.append(s[i])

w2=[c/i for i in w]
w_submm2=[c/i for i in w_submm]
s2=[i*1e-26 for i in s]
s_submm2=[i*1e-26 for i in s_submm]
integral2=np.trapz(w2,s2)

s3=[s[i]*1e-26*w2[i] for i in range(len(s))]

tbol=1.25e-11*np.trapz(w2,s3)/integral

lum=(integral2*4.0*m.pi*(dist*3.0857e16)**2)/L_sun

integral_submm=0.
for i in range(len(w_submm)-1):
	integral_submm+=1e-26*s_submm[i]*(abs((c/w_submm[i+1])-(c/w_submm[i]))) # calka pod wykresem 
#integral_submm=np.trapz(w_submm2,s_submm2)
# q=where(wl gt 349) gdzie lista dlugosci jest wieksza od 350 mikronow = L_bol_submm

lum_submm=((integral_submm)*4.0*m.pi*(dist*3.0857e16)**2)/L_sun

lum_submm_vel_lum=100.*(lum_submm/lum)


 

#------interpolation-----------------------------------


w3=w2[::-1]  #inverse list

#logaritmic scale
w2_log=[m.log10(freq) for freq in w2]
w3_log=[m.log10(freq) for freq in w3]
s_log=[m.log10(flux) for flux in s2]

interpolation_log=interp1d(w3_log, s_log, kind='linear', fill_value="extrapolate")


new_x_log=np.arange(w3_log[0],w3_log[-1],(w3_log[0]+w3_log[-1])/(100*len(w3_log)))
s_interpol_log=interpolation_log(new_x_log)

integral_interpol=0
for i in range(len(new_x_log)-1):
	integral_interpol+=1e-26*(10**s_interpol_log[i])*(abs((10**(new_x_log[i+1]))-(10**(new_x_log[i])))) # calka pod wykresem 

interpolation=interp1d(w2, s2, kind='cubic', fill_value="extrapolate")


new_x=np.arange(w3[0],w3[-1],(w3[0]+w3[-1])/(100*len(w3)))
s_interpol=interpolation(new_x)

interpolation_all=interp1d(all_points_freq, all_points_fluxes, kind='cubic', fill_value="extrapolate")


new_x_all=np.arange(all_points_freq[0],all_points_freq[-1],(all_points_freq[0]+all_points_freq[-1])/(100*len(all_points_freq)))
s_interpol_all=interpolation_all(new_x_all)



def integrate_function(function, start, end, steps=10000):
	sum_=0.
	dx=(end-start)/steps
	while start < end:
		sum_ += function(start)*dx
		start += dx
	return sum_
		 
def integrate(x, y):
	sum_=0.
	for i in range(1,len(x)):
		sum_ += ((y[i]+y[i-1])/2.)*(abs(x[i]-x[i-1]))
	return sum_

integral_interpol=integrate_function(interpolation, w3[0], w3[-1])

allpoints_integral=integrate_function(interpolation_all, w3[0], w3[-1])


s2_interpol=[s_interpol[i]*new_x[i] for i in range(len(s_interpol))]
s2_interpol_all=[s_interpol_all[i]*new_x[i] for i in range(len(s_interpol_all))]

flux_div_freq_log = [m.log10(s2[i]*w2[i]) for i in range(len(s2))] 
flux_div_freq_log_all = [m.log10(all_points_freq[i]*all_points_fluxes[i]) for i in range(len(all_points_freq))] 

tbol_interpol=(1.25e-11*integrate(new_x,s2_interpol))/integral_interpol
tbol_interpol_all=(1.25e-11*integrate(new_x_all,s2_interpol_all))/allpoints_integral

lum_interpol=(integral_interpol*4.0*m.pi*(dist*3.0857e16)**2)/L_sun
lum_interpol_all=(allpoints_integral*4.0*m.pi*(dist*3.0857e16)**2)/L_sun
print(lum_interpol, tbol_interpol)



newpoints_freq_log = [m.log10(freq) for freq in newpoints_freq]
newpoints_flux_div_freq_log = [m.log10(1e-26*newpoints_fluxes[i]*newpoints_freq[i]) for i in range(len(newpoints_fluxes))] 




fig=plt.figure()
plt.title('SMM1')
plt.ylabel(r'log(F $\cdot \nu$) [W $\cdot$ m$^2$]')
plt.xlabel(r'log($\nu$) [Hz]')
plt.plot(w2_log, flux_div_freq_log, 'ro', linewidth=1)
plt.plot(newpoints_freq_log, newpoints_flux_div_freq_log, 'bo', linewidth=1)

plt.savefig('smm1.png')
plt.close()

'''
#------calculate Lsubmm-----------------------------------

w_sbmm_interpol=loglev(minl=350,maxl=3.0e3,nlev=200)
s_sbmm_interpol=10.0^interpol(m.log10(w2), m.log10(s2), kind='cubic')
  
num=len(w)
integral=np.trapz(w_sbmm_interpol,s_sbmm_interpol)

lum_submm_interpol=(integral*4.0*m.pi*(dist*3.0857e16)**2)/3.86e26

  
lum_submm_vel_lum_interpol=100*lumsub_interpol/lum_interpol
  

print(lum_interpol, lum_submm_vel_lum_interpol)


'''

