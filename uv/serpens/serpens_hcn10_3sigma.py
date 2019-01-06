#-*-coding: utf-8-*-
'''
DESCRIPTION: This script displays the averaged and resampled spectrum (0.5 km/s)
DESCRIPTION: for a given region on map and plots 3*RMS and 1*RMS levels 
DESCRIPTION: and shows X ranges for flux calculation

The averaged region is consistent with HCN 1-0 beam size after convolution (27.8"), 
because it's the biggest for this molecule. We used the same beam size for other molecules.
'''

#!/usr/bin/python3.5

# name the output file
psname = 'smm1_hcn10_3s.eps'

# import packages
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import *
import pandas as pd

# ------------------------------------------------
# ------------------------------------------------
# find the x ranges (in km/s), which are above 3RMS
# level - for flux integration of line

rms = 1.343E-02 # rms taken from CLASS
rms_3 = 3*rms

# read the spectrum
spec_df = pd.read_table('serpens_hcn10_ave_spec.txt', delim_whitespace=True, header=None)

### 3 SIGMA ### 3 SIGMA ### 3 SIGMA ### 3 SIGMA ### 3 SIGMA ###
# left (x1) and right (x2) ranges in which we are looking for minima 
x1_ran_df = spec_df[(spec_df[0] > -5.0) & (spec_df[0] < -0.)]    #change ranges!! 
x2_ran_df = spec_df[(spec_df[0] > 10) & (spec_df[0] < 20.)]

#change ranges!!
# SERPENS HCN10: -5.0 - -0.0  and 10. - 20.

# for both X ranges take the column with flux and calculate abs(yi - 3rms)
y1_i_rms_3 = (x1_ran_df[1]-rms_3).abs()
y2_i_rms_3 = (x2_ran_df[1]-rms_3).abs()

# join two dataframes, reset and drop old index
# then change the names of column indexes from 011 to 123
final1_df = pd.concat([x1_ran_df, y1_i_rms_3], axis = 1).reset_index(drop=True)
final1_df.columns = [1,2,3]

final2_df = pd.concat([x2_ran_df, y2_i_rms_3], axis = 1).reset_index(drop=True)
final2_df.columns = [1,2,3]

# find the index of item which contains row with the minimum
min1 = final1_df[3].idxmin(axis=1, skipna=True)
min2 = final2_df[3].idxmin(axis=1, skipna=True)

# print the x value of minimum (in km/s)
print ('X1 (3s) =', final1_df[1].ix[min1].round(1))
print ('X2 (3s) =', final2_df[1].ix[min2].round(1))

# ------------------------------------------------
# ------------------------------------------------

### 1 SIGMA ### 1 SIGMA ### 1 SIGMA ### 1 SIGMA ### 1 SIGMA ###
# left (x3) and right (x4) ranges in which we are looking for minima 
x3_ran_df = spec_df[(spec_df[0] > -3.0) & (spec_df[0] < 0.0)]  #change ranges!!
x4_ran_df = spec_df[(spec_df[0] > 16.0) & (spec_df[0] < 17.1)]

#change ranges!!
# NGC1333 HCN10: -30.0 - -20.0  and -5. - -1.

# for both X ranges take the column with flux and calculate abs(yi - 3rms)
y3_i_rms = (x3_ran_df[1]-rms).abs()
y4_i_rms = (x4_ran_df[1]-rms).abs()

# join two dataframes, reset and drop old index

# then change the names of column indexes from 011 to 123
final3_df = pd.concat([x3_ran_df, y3_i_rms], axis = 1).reset_index(drop=True)
final3_df.columns = [1,2,3]

final4_df = pd.concat([x4_ran_df, y4_i_rms], axis = 1).reset_index(drop=True)
final4_df.columns = [1,2,3]

# find the index of item which contains row with the minimum
min3 = final3_df[3].idxmin(axis=1, skipna=True)
min4 = final4_df[3].idxmin(axis=1, skipna=True)

# print the x value of minimum (in km/s)
print ('X3 (1s) =', final3_df[1].ix[min3].round(1))
print ('X4 (1s) =', final4_df[1].ix[min4].round(1))

# ------------------------------------------------
# ------------------------------------------------


# ------------------------------------------------
# NOW PLOT THE SPEC WITH 3*RMS LEVEL AND X RANGES #
# ------------------------------------------------


fig = plt.figure(figsize = (9,7), dpi = 400)


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



""" READ INPUT DATA
########## SERPENS, HCN 1-0, center of ave.: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_hcn10, Tmb_hcn10 = loadtxt('serpens_hcn10_ave_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


ax = fig.add_subplot(111)


"""
CREATE A PLOT
"""
ax.set_xlabel(r'$\mathrm{V_{LSR}\;[km/s]}$', fontsize = 9)
ax.set_ylabel(r'$\mathrm{T_{MB}\;[K]}$', fontsize = 9)


# major x ticks every 20, minor ticks every 10
# major y ticks every 1, minor ticks every 0.5 
major_ticks_x = np.arange(-40, 50, 5)                                              
minor_ticks_x = np.arange(-40, 50, 1) 

major_ticks_y = np.arange(0.0, 1.2, 0.2)                                              
minor_ticks_y = np.arange(0.0, 1.2, 0.1) 

ax.set_xticks(major_ticks_x)                                                       
ax.set_xticks(minor_ticks_x, minor=True)

ax.set_yticks(major_ticks_y)                                                       
ax.set_yticks(minor_ticks_y, minor=True)

# Set the tick labels font
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(7)


"""
########## SERPENS, HCN 1-0, center of ave.: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax.plot(v_hcn10, Tmb_hcn10, color = 'black', linewidth=1.0, linestyle = '-')
plt.axhline(y=rms_3, xmin = -60.0, xmax = 40.0, color = 'red', linewidth=1.5, linestyle = '-')
plt.axhline(y=rms, xmin = -60.0, xmax = 40.0, color = 'green', linewidth=1.5, linestyle = '-')

# THE ANNOTATIONS ON A GRAPH
#---------------------------
# alpha - transparency, fc - a color of inner part of arrow, ec - a color of an edge of arrow
# headwidth - the size of arrow, frac - a lenght of the head of arrow
# shrink - fraction of total length to ‘shrink’ from both ends
#ax.annotate(r'$\mathrm{RMS\;=%.5f\;K;3*RMS\;=%.3f\;K}$'%(rms,rms_3), fontsize=10, xy=(-38.0, 1.13), textcoords='data')
#ax.annotate(r'$\mathrm{set\;window\;-30\;40}$', fontsize=10, xy=(-38.0, 1.1), textcoords='data')
#ax.annotate(r'$\mathrm{X_{1}\;(3s)\;=%.1f \;km/s}$'%(final1_df[1].ix[min1].round(1)), fontsize=10, xy=(-38.0, 1.07), textcoords='data')
#ax.annotate(r'$\mathrm{X_{2}\;(3s)\;=%.1f \;km/s}$'%(final2_df[1].ix[min2].round(1)), fontsize=10, xy=(-38.0, 1.04), textcoords='data')
#ax.annotate(r'$\mathrm{X_{3}\;(1s)\;=%.1f \;km/s}$'%(final3_df[1].ix[min3].round(1)), fontsize=10, xy=(-38.0, 1.01), textcoords='data')
#ax.annotate(r'$\mathrm{X_{4}\;(1s)\;=%.1f \;km/s}$'%(final4_df[1].ix[min4].round(1)), fontsize=10, xy=(-38.0, 0.98), textcoords='data')


# plot the vertical lines for x = min1 and x = min2
plt.axvline(x=final1_df[1].ix[min1].round(1), color='red', linestyle='--')
plt.axvline(x=final2_df[1].ix[min2].round(1), color='red', linestyle='--')

# plot the vertical lines for x = min3 and x = min4
plt.axvline(x=final3_df[1].ix[min3].round(1), color='green', linestyle='--')
plt.axvline(x=final4_df[1].ix[min4].round(1), color='green', linestyle='--')



# the upper and lower axis limits on a LEFT GRAPH
ax.set_xlim([-40.0, 50.0])
ax.set_ylim([-0.1, 1.2])


# close and save file
savefig(psname, format = 'eps', bbox_inches = 'tight') 
clf()
