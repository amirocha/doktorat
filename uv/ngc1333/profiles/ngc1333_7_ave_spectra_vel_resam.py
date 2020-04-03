'''
DESCRIPTION: This script displays the resampled profiles (0.5 km/s)
DESCRIPTION: of diff. molecules for 14 diff. positions in SERPENS

The averaged region is consistent with HCN 1-0 beam size (27.8"), 
because it's the biggest for this molecule. We used the same 
beam size for other molecules.
'''

#!/usr/bin/python3.3

# name the output file
psname = 'ngc1333_spectra_3.eps'

# import packages
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import *

fig = plt.figure(figsize = (20,10), dpi = 400)



#plt.rcParams["font.family"] = "Times New Roman"
rc('font', **{'family':'serif', 'serif':['Times New Roman']})
params = {'backend': 'pdf',
          #'axes.labelsize': 12,
          #'text.fontsize': 12,
          #'legend.fontsize': 12,
          #'xtick.labelsize': 7,
          #'ytick.labelsize': 7,
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

plt.tick_params(axis='y',          # changes apply to the y-axis only
    which='both',      # both major and minor ticks are affected
    right=False)      # ticks along the bottom edge are off
            # ticks along the top edge are off  x-axis:bottom/top=False

""" FIRST PANEL - READ INPUT DATA
########## C34S 3-2 ##########
"""
v_c34s32_p1, Tmb_c34s32_p1 = loadtxt('./ngc1333_c34s32_SVS13.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## CS 3-2 ##########
"""
v_cs32_p1, Tmb_cs32_p1 = loadtxt('./ngc1333_cs32_SVS13.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## H13CN 1-0 ##########
"""
v_h13cn10_p1, Tmb_h13cn10_p1 = loadtxt('./ngc1333_h13cn10_SVS13.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
##########  HCN 1-0 ##########
"""
v_hcn10_p1, Tmb_hcn10_p1 = loadtxt('./ngc1333_hcn10_SVS13.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## CN 1-0 ##########
"""
v_cn10_p1, Tmb_cn10_p1 = loadtxt('./ngc1333_cn10_SVS13.txt', usecols=(0, 1), unpack=True, skiprows=1)


ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)


# remove empty space between subplots
#fig.subplots_adjust(hspace=.1) # height spaces
fig.subplots_adjust(wspace=0) # width spaces



"""
FIRST PANEL - CREATE A PLOT
"""
#ax1.set_xlabel(r'$\mathrm{V_{LSR}\;[km/s]}$', fontsize = 14)
ax1.set_ylabel(r'$T_\mathrm{MB}$ [K] + Offset', fontsize = 14)


# major x ticks every 20, minor ticks every 10
# major y ticks every 1, minor ticks every 0.5 
major_ticks_x = np.arange(-80, 35, 20)                                              
minor_ticks_x = np.arange(-80, 35, 10) 

major_ticks_y = np.arange(0.0, 32, 4.0)                                              
minor_ticks_y = np.arange(0.0, 32, 0.5) 

ax1.set_xticks(major_ticks_x)                                                       
ax1.set_xticks(minor_ticks_x, minor=True)

ax1.set_yticks(major_ticks_y)                                                       
ax1.set_yticks(minor_ticks_y, minor=True)

# Set the tick labels font
for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(12)

ax1.axvline(x=7.2, linewidth=0.7)



"""
########## C34S 3-2 (x 3) ##########
"""
ax1.plot(v_c34s32_p1, 3*(Tmb_c34s32_p1) + 16.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=16, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## CS 3-2 ##########
"""
ax1.plot(v_cs32_p1, Tmb_cs32_p1 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=12, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## H13CN 1-0 ##########
"""
ax1.plot(v_h13cn10_p1, 5*(Tmb_h13cn10_p1) + 8.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=8, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## HCN 1-0 ##########
"""
ax1.plot(v_hcn10_p1, Tmb_hcn10_p1 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## CN 1-0 ##########
"""
ax1.plot(v_cn10_p1, Tmb_cn10_p1, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

ax1.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 18.0), textcoords='data')
ax1.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.), textcoords='data')
ax1.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 10.0), textcoords='data')
ax1.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 5.5), textcoords='data')
ax1.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax1.annotate(r'$\mathrm{SVS\;13}$', color='blue', fontsize=18, xy=(-30.0, 20), textcoords='data')



# the upper and lower axis limits on a LEFT GRAPH
ax1.set_xlim([-90.0, 40.0])
ax1.set_ylim([-0.5, 22.5])





major_ticks_x = ([])                                              
minor_ticks_x = ([])
major_ticks_y = ([])                                              
minor_ticks_y = ([])  

ax2.set_xticks(major_ticks_x)                                                       
ax2.set_xticks(minor_ticks_x, minor=True)

ax2.set_yticks(major_ticks_y)                                                       
ax2.set_yticks(minor_ticks_y, minor=True)




# the upper and lower axis limits on a RIGHT GRAPH
ax2.set_xlim([-90.0, 40.0])
ax2.set_ylim([-0.5, 22.5])


major_ticks_x = ([])                                              
minor_ticks_x = ([])
major_ticks_y = ([])                                              
minor_ticks_y = ([])

ax3.set_xticks(major_ticks_x)                                                       
ax3.set_xticks(minor_ticks_x, minor=True)

ax3.set_yticks(major_ticks_y)                                                       
ax3.set_yticks(minor_ticks_y, minor=True)


# the upper and lower axis limits on a RIGHT GRAPH
ax3.set_xlim([-90.0, 40.0])
ax3.set_ylim([-0.5, 22.5])


# close and save file
savefig(psname, format = 'eps', bbox_inches = 'tight') 
clf()
