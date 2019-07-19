#!/usr/bin/python3.3

# name the output file
psname = 'serpens_seds.eps'

# import packages
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import *

fig = plt.figure(figsize = (5,8), dpi = 400)


#plt.rcParams["font.family"] = "Times New Roman"
rc('font', **{'family':'serif', 'serif':['Times New Roman']})
params = {'backend': 'pdf',
          'axes.labelsize': 12,
          #'text.fontsize': 12,
          #'legend.fontsize': 12,
          'xtick.labelsize': 20,
          'ytick.labelsize': 12,
          # The comm. below determines whether you use LaTeX 
          # for all text in matplotlib (you probably don't want 
          # to turn this on, but may)
          'text.usetex': False,
          # four comm. below (math) determines what is used for math rendering 
          'mathtext.rm': 'serif',
          'mathtext.it': 'serif:italic',
          'mathtext.bf': 'serif:bold',
          'mathtext.fontset': 'custom',
          #'figure.figsize': fig_size,
          'axes.unicode_minus': True}
matplotlib.rcParams.update(params)



""" FIRST PANEL - READ INPUT DATA
########## SERPENS, SMM1 ##########
"""
v_smm1, f_smm1 = loadtxt('./sed_smm1_photo.txt', usecols=(0, 1), unpack=True, skiprows=1) #frequency / flux (log scale)


"""
########## SERPENS, SMM2 ##########
"""
v_smm2, f_smm2 = loadtxt('./sed_smm2.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, SMM3 ##########
"""
v_smm3, f_smm3 = loadtxt('./sed_smm3_photo.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, SMM4 ##########
"""
v_smm4, f_smm4 = loadtxt('./sed_smm4_photo.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, SMM5 ##########
"""
v_smm5, f_smm5 = loadtxt('./sed_smm5.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, SMM6 ##########
"""
v_smm6, f_smm6 = loadtxt('./sed_smm6.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, SMM9 ##########
"""
v_smm9, f_smm9 = loadtxt('./sed_smm9.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, SMM10 ##########
"""
v_smm10, f_smm10 = loadtxt('./sed_smm10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, SMM12 ##########
"""
v_smm12, f_smm12 = loadtxt('./sed_smm12.txt', usecols=(0, 1), unpack=True, skiprows=1)


ax1 = plt.subplot(1, 1, 1)



# remove empty space between subplots
#fig.subplots_adjust(hspace=.1) # height spaces
fig.subplots_adjust(wspace=0.15) # width spaces



"""
FIRST PANEL - CREATE A PLOT
"""
ax1.set_xlabel(r'$\mathrm{log(\nu)\;[Hz]}$', fontsize = 14)
ax1.set_ylabel(r'$\mathrm{Log(F)\;[W\,m^{-2}\,Hz^{-1}]\;\,+\,Offset}$', fontsize = 14)


# major x ticks every 20, minor ticks every 10
# major y ticks every 1, minor ticks every 0.5 
major_ticks_x = np.arange(10, 15, 1)                                              
minor_ticks_x = np.arange(10, 15, 0.1) 

major_ticks_y = np.arange(-28, 5, 2.0)                                              
minor_ticks_y = np.arange(-28, 5, 0.5) 

ax1.set_xticks(major_ticks_x)                                                       
ax1.set_xticks(minor_ticks_x, minor=True)

ax1.set_yticks(major_ticks_y)                                                       
ax1.set_yticks(minor_ticks_y, minor=True)

# Set the tick labels font
for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(10)



"""
########## SERPENS, SMM1 ##########
"""
ax1.plot(v_smm1, f_smm1 + 24.0, 'bo')


"""
########## SERPENS, SMM2 ##########
"""
ax1.plot(v_smm2, f_smm2 + 21, 'ro')


"""
########## SERPENS, SMM3 ##########
"""
ax1.plot(v_smm3, f_smm3 + 18.0, 'ko')


"""
########## SERPENS, SMM4 ##########
"""
ax1.plot(v_smm4, f_smm4 + 15, 'bo')


"""
########## SERPENS, SMM5 ##########
"""
ax1.plot(v_smm5, f_smm5 + 12.0, 'ro')


"""
########## SERPENS, SMM6 ##########
"""
ax1.plot(v_smm6, f_smm6 + 9, 'ko')


"""
########## SERPENS, SMM9 ##########
"""
ax1.plot(v_smm9, f_smm9 + 6.0, 'bo')


"""
########## SERPENS, SMM10 ##########
"""
ax1.plot(v_smm10, f_smm10 + 3, 'ro')


"""
########## SERPENS, SMM12 ##########
"""
ax1.plot(v_smm12, f_smm12, 'ko')



ax1.annotate(r'$\mathrm{SMM1}$', fontsize=12, xy=(10.3, -1.0), textcoords='data')
ax1.annotate(r'$\mathrm{SMM2}$', fontsize=12, xy=(10.3, -5), textcoords='data')
ax1.annotate(r'$\mathrm{SMM3}$', fontsize=12, xy=(10.3, -8), textcoords='data')
ax1.annotate(r'$\mathrm{SMM4}$', fontsize=12, xy=(10.3, -11), textcoords='data')
ax1.annotate(r'$\mathrm{SMM5}$', fontsize=12, xy=(10.3, -14), textcoords='data')
ax1.annotate(r'$\mathrm{SMM6}$', fontsize=12, xy=(10.3, -16), textcoords='data')
ax1.annotate(r'$\mathrm{SMM9}$', fontsize=12, xy=(10.3, -19), textcoords='data')
ax1.annotate(r'$\mathrm{SMM10}$', fontsize=12, xy=(10.3, -22), textcoords='data')
ax1.annotate(r'$\mathrm{SMM12}$', fontsize=12, xy=(10.3, -25), textcoords='data')
#ax1.annotate(r'$\mathrm{SED}$', color='red', fontsize=18, xy=(12.5, 3), textcoords='data')



# the upper and lower axis limits on a LEFT GRAPH
ax1.set_xlim([10.0, 15.0])
ax1.set_ylim([-28.5, 2])





# close and save file
savefig(psname, format = 'eps', bbox_inches = 'tight') 
clf()
