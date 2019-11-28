'''
DESCRIPTION: This script displays the resampled profiles (0.5 km/s)
DESCRIPTION: of diff. molecules for 14 diff. positions in SERPENS

The averaged region is consistent with HCN 1-0 beam size (27.8"), 
because it's the biggest for this molecule. We used the same 
beam size for other molecules.
'''

#!/usr/bin/python3.3

# name the output file
psname = 'serpens_spectra_1.eps'

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

ax1.axvline(x=8.5, linewidth=0.7)


"""
########## SERPENS, CO ,- center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax1.plot(v_co65_p1, Tmb_co65_p1 + 22, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=22, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

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
ax1.plot(v_cn10_p1, Tmb_cn10_p1, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')




ax1.annotate(r'$\mathrm{CO\;\;6-5}$', fontsize=14, xy=(-85.0, 25), textcoords='data')
ax1.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax1.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax1.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data'
#)
ax1.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax1.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax1.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax1.annotate(r'$\mathrm{SMM1}$', color='blue', fontsize=18, xy=(-30.0, 28.5), textcoords='data')



# the upper and lower axis limits on a LEFT GRAPH
ax1.set_xlim([-90.0, 40.0])
ax1.set_ylim([-0.5, 32.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" SECOND PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
v_c34s32_p2, Tmb_c34s32_p2 = loadtxt('./serpens_c34s32_smm2.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
v_cs32_p2, Tmb_cs32_p2 = loadtxt('./serpens_cs32_smm2.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
##v_h13cn21_p2, Tmb_h13cn21_p2 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_128.6_156.4_-140.1_-112.3_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
v_h13cn10_p2, Tmb_h13cn10_p2 = loadtxt('./serpens_h13cn10_smm2.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
v_hcn10_p2, Tmb_hcn10_p2 = loadtxt('./serpens_hcn10_smm2.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
v_cn10_p2, Tmb_cn10_p2 = loadtxt('./serpens_cn10_smm2.txt', usecols=(0, 1), unpack=True, skiprows=1)

"""
########## SERPENS, CO 6-5, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_co65_p2, Tmb_co65_p2 = loadtxt('./serpens_co65_smm2.txt', usecols=(0, 1), unpack=True, skiprows=1)



"""
SECOND PANEL - CREATE A PLOT
"""
#ax2.set_xlabel(r'$\mathrm{V_{LSR}\;[km/s]}$', fontsize = 14)


# major x ticks every 20, minor ticks every 10
# major y ticks every 1, minor ticks every 0.5 
major_ticks_x = np.arange(-80, 35, 20)                                              
minor_ticks_x = np.arange(-80, 35, 10) 

major_ticks_y = ([])                                              
minor_ticks_y = ([])  

ax2.set_xticks(major_ticks_x)                                                       
ax2.set_xticks(minor_ticks_x, minor=True)

ax2.set_yticks(major_ticks_y)                                                       
ax2.set_yticks(minor_ticks_y, minor=True)

# Set the tick labels font
for label in (ax2.get_xticklabels() + ax2.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(12)

ax2.axvline(x=7.6, linewidth=0.7)

"""
########## SERPENS, C34S 3-2 (x 3), center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
ax2.plot(v_c34s32_p2, 3*(Tmb_c34s32_p2) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
ax2.plot(v_cs32_p2, Tmb_cs32_p2 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
#

#ax2.plot(v_h13cn21_p2, Tmb_h13cn21_p2 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
ax2.plot(v_h13cn10_p2, 5*(Tmb_h13cn10_p2) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
ax2.plot(v_hcn10_p2, Tmb_hcn10_p2 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 142.5 -126.2, range: 128.6 156.4 -140.1 -112.3 ##########
"""
ax2.plot(v_cn10_p2, Tmb_cn10_p2, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CO ,- center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax2.plot(v_co65_p2, Tmb_co65_p2 + 22, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=22, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')


ax2.annotate(r'$\mathrm{CO\;\;6-5}$', fontsize=14, xy=(-85.0, 25), textcoords='data')
ax2.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax2.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax2.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data'
#)
ax2.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax2.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax2.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax2.annotate(r'$\mathrm{SMM2}$', color='blue', fontsize=18, xy=(-30.0, 28.5), textcoords='data')



# the upper and lower axis limits on a RIGHT GRAPH
ax2.set_xlim([-90.0, 40.0])
ax2.set_ylim([-0.5, 32.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" THIRD PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
v_c34s32_p3, Tmb_c34s32_p3 = loadtxt('./serpens_c34s32_smm3.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
v_cs32_p3, Tmb_cs32_p3 = loadtxt('./serpens_cs32_smm3.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
##v_h13cn21_p3, Tmb_h13cn21_p3 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_107.823_135.623_-127.242_-99.442_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
v_h13cn10_p3, Tmb_h13cn10_p3 = loadtxt('./serpens_h13cn10_smm3.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
v_hcn10_p3, Tmb_hcn10_p3 = loadtxt('./serpens_hcn10_smm3.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
v_cn10_p3, Tmb_cn10_p3 = loadtxt('./serpens_cn10_smm3.txt', usecols=(0, 1), unpack=True, skiprows=1)

"""
########## SERPENS, CO 6-5, center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
v_co65_p3, Tmb_co65_p3 = loadtxt('./serpens_co65_smm3.txt', usecols=(0, 1), unpack=True, skiprows=1)



"""
THIRD PANEL - CREATE A PLOT
"""

#ax3.set_xlabel(r'$\mathrm{V_{LSR}\;[km/s]}$', fontsize = 14)


# major x ticks every 20, minor ticks every 10
# major y ticks every 1, minor ticks every 0.5 
major_ticks_x = np.arange(-80, 35, 20)                                              
minor_ticks_x = np.arange(-80, 35, 10) 

major_ticks_y = ([])                                              
minor_ticks_y = ([])

ax3.set_xticks(major_ticks_x)                                                       
ax3.set_xticks(minor_ticks_x, minor=True)

ax3.set_yticks(major_ticks_y)                                                       
ax3.set_yticks(minor_ticks_y, minor=True)

# Set the tick labels font
for label in (ax3.get_xticklabels() + ax3.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(12)

ax3.axvline(x=7.6, linewidth=0.7)

"""
########## SERPENS, C34S 3-2 (x 3), center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
ax3.plot(v_c34s32_p3, 3*(Tmb_c34s32_p3) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')


"""
########## SERPENS, CS 3-2, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
ax3.plot(v_cs32_p3, Tmb_cs32_p3 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
##ax3.plot(v_h13cn21_p3, Tmb_h13cn21_p3 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
ax3.plot(v_h13cn10_p3, 5*(Tmb_h13cn10_p3) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
ax3.plot(v_hcn10_p3, Tmb_hcn10_p3 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 121.723 -113.342, range: 107.823 135.623 -127.242 -99.442 ##########
"""
ax3.plot(v_cn10_p3, Tmb_cn10_p3, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CO ,- center: 163.5 -142.7, range: 149.6 177.4 -156.6 -128.8 ##########
"""
ax3.plot(v_co65_p3, Tmb_co65_p3 + 22, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=22, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

ax3.annotate(r'$\mathrm{CO\;\;6-5}$', fontsize=14, xy=(-85.0, 25), textcoords='data')
ax3.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax3.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax3.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax3.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax3.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax3.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax3.annotate(r'$\mathrm{SMM3}$', color='blue', fontsize=18, xy=(-30.0, 28.5), textcoords='data')


# the upper and lower axis limits on a RIGHT GRAPH
ax3.set_xlim([-90.0, 40.0])
ax3.set_ylim([-0.5, 32.5])


# close and save file
savefig(psname, format = 'eps', bbox_inches = 'tight') 
clf()
