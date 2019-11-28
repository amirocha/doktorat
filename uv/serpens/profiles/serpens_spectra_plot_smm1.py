'''
DESCRIPTION: This script displays the resampled profiles (0.5 km/s)
DESCRIPTION: of diff. molecules for 14 diff. positions in SERPENS

The averaged region is consistent with HCN 1-0 beam size (27.8"), 
because it's the biggest for this molecule. We used the same 
beam size for other molecules.
'''

#!/usr/bin/python3.3

# name the output file
psname = 'serpens_spectra_smm1_narrow.eps'

# import packages
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import *

fig = plt.figure(figsize = (10,40), dpi = 400)
plt.tight_layout()



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
########## SERPENS, C34S 3-2, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_c34s32_p1, Tmb_c34s32_p1 = loadtxt('./serpens_c34s32_smm1.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_cs32_p1, Tmb_cs32_p1 = loadtxt('./serpens_cs32_smm1.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
##v_h13cn21_p1, Tmb_h13cn21_p1 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_149.6_177.4_-156.6_-128.8_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_h13cn10_p1, Tmb_h13cn10_p1 = loadtxt('./serpens_h13cn10_smm1.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_hcn10_p1, Tmb_hcn10_p1 = loadtxt('./serpens_hcn10_smm1.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_cn10_p1, Tmb_cn10_p1 = loadtxt('./serpens_cn10_smm1.txt', usecols=(0, 1), unpack=True, skiprows=1)

"""
########## SERPENS, CO 6-5, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_co65_p1, Tmb_co65_p1 = loadtxt('./serpens_co65_smm1.txt', usecols=(0, 1), unpack=True, skiprows=1)

"""
########## SERPENS, C18O 6-5, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_c18o65_p1, Tmb_c18o65_p1 = loadtxt('./serpens_c18o65_smm1.txt', usecols=(0, 1), unpack=True, skiprows=1)

ax1 = plt.subplot(1, 1, 1)


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
major_ticks_x = np.arange(0, 20, 20)                                              
minor_ticks_x = np.arange(0, 20, 10) 

major_ticks_y = np.arange(0.0, 32, 4.0)                                              
minor_ticks_y = np.arange(0.0, 32, 0.5) 

ax1.set_xticks(major_ticks_x)                                                       
ax1.set_xticks(minor_ticks_x, minor=True)

ax1.set_yticks(major_ticks_y)                                                       
ax1.set_yticks(minor_ticks_y, minor=True)

ax1.axvline(x=8.5, linewidth=0.7)
ax1.axvline(x=7.8, linewidth=0.7, c='red')
ax1.axvline(x=9.4, linewidth=0.7, c='red')

# Set the tick labels font
for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(12)



"""
########## SERPENS, C34S 3-2 (x 3), center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax1.plot(v_c34s32_p1, 3*(Tmb_c34s32_p1) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax1.plot(v_cs32_p1, Tmb_cs32_p1 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
##ax1.plot(v_h13cn21_p1, Tmb_h13cn21_p1 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax1.plot(v_h13cn10_p1, 5*(Tmb_h13cn10_p1) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax1.plot(v_hcn10_p1, Tmb_hcn10_p1 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax1.plot(v_cn10_p1, 2*Tmb_cn10_p1, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CO ,- center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax1.plot(v_co65_p1, Tmb_co65_p1/2 + 22, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=22, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, C18O ,- center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax1.plot(v_c18o65_p1, Tmb_c18o65_p1*5 + 29, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=29, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

ax1.annotate(r'$\mathrm{C^{18}O\;\;6-5\;(\times5)}$', fontsize=14, xy=(-85.0, 31), textcoords='data')
ax1.annotate(r'$\mathrm{CO\;\;6-5\;(\div2)}$', fontsize=14, xy=(-85.0, 25), textcoords='data')
ax1.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=14, xy=(-85.0, 20.0), textcoords='data')
ax1.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=14, xy=(-85.0, 14.4), textcoords='data')
#ax1.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data'
#)
ax1.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=14, xy=(-85.0, 12.0), textcoords='data')
ax1.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=14, xy=(-85.0, 4.5), textcoords='data')
ax1.annotate(r'$\mathrm{CN\;\;1-0\;(\times2)}$', fontsize=14, xy=(-85.0, 1.7), textcoords='data')
ax1.annotate(r'$\mathrm{Protostar}$', color='blue', fontsize=18, xy=(-35.0, 34.5), textcoords='data')



# the upper and lower axis limits on a LEFT GRAPH
ax1.set_xlim([0.0, 20.0])
ax1.set_ylim([-0.5, 32])



# close and save file
savefig(psname, format = 'eps', bbox_inches = 'tight') 
clf()
