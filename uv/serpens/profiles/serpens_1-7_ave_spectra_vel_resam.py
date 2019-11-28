'''
DESCRIPTION: This script displays the resampled profiles (0.5 km/s)
DESCRIPTION: of diff. molecules for 14 diff. positions in SERPENS

The averaged region is consistent with HCN 1-0 beam size (27.8"), 
because it's the biggest for this molecule. We used the same 
beam size for other molecules.
'''

#!/usr/bin/python3.3

# name the output file
psname = 'serpens_1-3_spectra_vel_resam.eps'

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



ax1 = plt.subplot(1, 7, 1)
ax2 = plt.subplot(1, 7, 2)
ax3 = plt.subplot(1, 7, 3)
ax4 = plt.subplot(1, 7, 4)
ax5 = plt.subplot(1, 7, 5)
ax6 = plt.subplot(1, 7, 6)
ax7 = plt.subplot(1, 7, 7)

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

major_ticks_y = np.arange(0.0, 23, 4.0)                                              
minor_ticks_y = np.arange(0.0, 22, 0.5) 

ax1.set_xticks(major_ticks_x)                                                       
ax1.set_xticks(minor_ticks_x, minor=True)

ax1.set_yticks(major_ticks_y)                                                       
ax1.set_yticks(minor_ticks_y, minor=True)

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
ax1.plot(v_cn10_p1, Tmb_cn10_p1, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')


ax1.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax1.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax1.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data'
#)
ax1.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax1.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax1.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax1.annotate(r'$\mathrm{SMM1}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')



# the upper and lower axis limits on a LEFT GRAPH
ax1.set_xlim([-90.0, 40.0])
ax1.set_ylim([-0.5, 22.5])





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
v_cs32_p2, Tmb_cs32_p2 = loadtxt('./serpens_cs32_smm1.txt', usecols=(0, 1), unpack=True, skiprows=1)


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


ax2.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax2.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax2.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data'
#)
ax2.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax2.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax2.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax2.annotate(r'$\mathrm{SMM2}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')



# the upper and lower axis limits on a RIGHT GRAPH
ax2.set_xlim([-90.0, 40.0])
ax2.set_ylim([-0.5, 22.5])





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


ax3.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax3.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax3.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax3.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax3.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax3.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax3.annotate(r'$\mathrm{SMM3}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')


# the upper and lower axis limits on a RIGHT GRAPH
ax3.set_xlim([-90.0, 40.0])
ax3.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" FOURTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
v_c34s32_p4, Tmb_c34s32_p4 = loadtxt('./serpens_c34s32_smm4.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
v_cs32_p4, Tmb_cs32_p4 = loadtxt('./serpens_cs32_smm4.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
##v_h13cn21_p4, Tmb_h13cn21_p4 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_92.6_120.4_-137.2_-109.4_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
v_h13cn10_p4, Tmb_h13cn10_p4 = loadtxt('./serpens_h13cn10_smm4.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
v_hcn10_p4, Tmb_hcn10_p4 = loadtxt('./serpens_hcn10_smm4.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
v_cn10_p4, Tmb_cn10_p4 = loadtxt('./serpens_cn10_smm4.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
FOURTH PANEL - CREATE A PLOT
"""

ax4.set_xlabel(r'$v_\mathrm{LSR}\;$[km s$^{-1}$]', fontsize = 14)


# major x ticks every 20, minor ticks every 10
# major y ticks every 1, minor ticks every 0.5 
major_ticks_x = np.arange(-80, 35, 20)                                              
minor_ticks_x = np.arange(-80, 35, 10) 

major_ticks_y = ([])                                             
minor_ticks_y = ([]) 

ax4.set_xticks(major_ticks_x)                                                       
ax4.set_xticks(minor_ticks_x, minor=True)

ax4.set_yticks(major_ticks_y)                                                       
ax4.set_yticks(minor_ticks_y, minor=True)

# Set the tick labels font
for label in (ax4.get_xticklabels() + ax4.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(12)



"""
########## SERPENS, C34S 3-2 (x 3), center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
ax4.plot(v_c34s32_p4, 3*(Tmb_c34s32_p4) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
ax4.plot(v_cs32_p4, Tmb_cs32_p4 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
##ax4.plot(v_h13cn21_p4, Tmb_h13cn21_p4 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
ax4.plot(v_h13cn10_p4, 5*(Tmb_h13cn10_p4) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
ax4.plot(v_hcn10_p4, Tmb_hcn10_p4 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 106.5 -123.3, range: 92.6 120.4 -137.2 -109.4 ##########
"""
ax4.plot(v_cn10_p4, Tmb_cn10_p4, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')


ax4.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax4.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax4.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data'
#)
ax4.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax4.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax4.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax4.annotate(r'$\mathrm{SMM4}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')


# the upper and lower axis limits on a RIGHT GRAPH
ax4.set_xlim([-90.0, 40.0])
ax4.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" FIFTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
v_c34s32_p5, Tmb_c34s32_p5 = loadtxt('./serpens_c34s32_smm5.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
v_cs32_p5, Tmb_cs32_p5 = loadtxt('./serpens_cs32_smm5.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
##v_h13cn21_p5, Tmb_h13cn21_p5 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_92.636_120.436_-123.2_-95.4_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
v_h13cn10_p5, Tmb_h13cn10_p5 = loadtxt('./serpens_h13cn10_smm5.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
v_hcn10_p5, Tmb_hcn10_p5 = loadtxt('./serpens_hcn10_smm5.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
v_cn10_p5, Tmb_cn10_p5 = loadtxt('./serpens_cn10_smm5.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
FIFTH PANEL - CREATE A PLOT
"""
#ax5.set_xlabel(r'$\mathrm{V_{LSR}\;[km/s]}$', fontsize = 14)


# major x ticks every 20, minor ticks every 10
# major y ticks every 1, minor ticks every 0.5 
major_ticks_x = np.arange(-80, 35, 20)                                              
minor_ticks_x = np.arange(-80, 35, 10) 

major_ticks_y = ([])                                              
minor_ticks_y = ([]) 

ax5.set_xticks(major_ticks_x)                                                       
ax5.set_xticks(minor_ticks_x, minor=True)

ax5.set_yticks(major_ticks_y)                                                       
ax5.set_yticks(minor_ticks_y, minor=True)

# Set the tick labels font
for label in (ax5.get_xticklabels() + ax5.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(12)


"""
########## SERPENS, C34S 3-2 (x 3), center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
ax5.plot(v_c34s32_p5, 3*(Tmb_c34s32_p5) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
ax5.plot(v_cs32_p5, Tmb_cs32_p5 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
##ax5.plot(v_h13cn21_p5, Tmb_h13cn21_p5 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
ax5.plot(v_h13cn10_p5, 5*(Tmb_h13cn10_p5) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
ax5.plot(v_hcn10_p5, Tmb_hcn10_p5 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 106.536 -109.3, range: 92.636 120.436 -123.2 -95.4 ##########
"""
ax5.plot(v_cn10_p5, Tmb_cn10_p5, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')


ax5.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax5.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax5.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax5.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax5.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax5.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax5.annotate(r'$\mathrm{SMM5}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')


# the upper and lower axis limits on a RIGHT GRAPH
ax5.set_xlim([-90.0, 40.0])
ax5.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" SIXTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
v_c34s32_p6, Tmb_c34s32_p6 = loadtxt('./serpens_c34s32_smm6.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
v_cs32_p6, Tmb_cs32_p6 = loadtxt('./serpens_cs32_smm6.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
##v_h13cn21_p6, Tmb_h13cn21_p6 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_48.686_76.486_-123.2_-95.4_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
v_h13cn10_p6, Tmb_h13cn10_p6 = loadtxt('./serpens_h13cn10_smm6.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
v_hcn10_p6, Tmb_hcn10_p6 = loadtxt('./serpens_hcn10_smm6.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
v_cn10_p6, Tmb_cn10_p6 = loadtxt('./serpens_cn10_smm6.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
SIXTH PANEL - CREATE A PLOT
"""
#ax6.set_xlabel(r'$\mathrm{V_{LSR}\;[km/s]}$', fontsize = 14)


# major x ticks every 20, minor ticks every 10
# major y ticks every 1, minor ticks every 0.5 
major_ticks_x = np.arange(-80, 35, 20)                                              
minor_ticks_x = np.arange(-80, 35, 10) 

major_ticks_y = ([])                                             
minor_ticks_y = ([]) 

ax6.set_xticks(major_ticks_x)                                                       
ax6.set_xticks(minor_ticks_x, minor=True)

ax6.set_yticks(major_ticks_y)                                                       
ax6.set_yticks(minor_ticks_y, minor=True)

# Set the tick labels font
for label in (ax6.get_xticklabels() + ax6.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(12)


"""
########## SERPENS, C34S 3-2 (x 3), center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
ax6.plot(v_c34s32_p6, 3*(Tmb_c34s32_p6) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
ax6.plot(v_cs32_p6, Tmb_cs32_p6 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
##ax6.plot(v_h13cn21_p6, Tmb_h13cn21_p6 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
ax6.plot(v_h13cn10_p6, 5*(Tmb_h13cn10_p6) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
ax6.plot(v_hcn10_p6, Tmb_hcn10_p6 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 62.586 -109.3, range: 48.686 76.486 -123.2 -95.4 ##########
"""
ax6.plot(v_cn10_p6, Tmb_cn10_p6, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')


ax6.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax6.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax6.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data'
#)
ax6.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax6.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax6.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax6.annotate(r'$\mathrm{SMM6}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')


# the upper and lower axis limits on a RIGHT GRAPH
ax6.set_xlim([-90.0, 40.0])
ax6.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" SEVENTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
v_c34s32_p7, Tmb_c34s32_p7 = loadtxt('./serpens_c34s32_smm9.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
v_cs32_p7, Tmb_cs32_p7 = loadtxt('./serpens_cs32_smm9.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
##v_h13cn21_p7, Tmb_h13cn21_p7 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_131.6_159.4_-92.7_-64.9_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
v_h13cn10_p7, Tmb_h13cn10_p7 = loadtxt('./serpens_h13cn10_smm9.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
v_hcn10_p7, Tmb_hcn10_p7 = loadtxt('./serpens_hcn10_smm9.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
v_cn10_p7, Tmb_cn10_p7 = loadtxt('./serpens_cn10_smm9.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
SEVENTH PANEL - CREATE A PLOT
"""
#ax7.set_xlabel(r'$\mathrm{V_{LSR}\;[km/s]}$', fontsize = 14)


# major x ticks every 20, minor ticks every 10
# major y ticks every 1, minor ticks every 0.5 
major_ticks_x = np.arange(-80, 35, 20)                                              
minor_ticks_x = np.arange(-80, 35, 10) 

major_ticks_y = ([])                                              
minor_ticks_y = ([])

ax7.set_xticks(major_ticks_x)                                                       
ax7.set_xticks(minor_ticks_x, minor=True)

ax7.set_yticks(major_ticks_y)                                                       
ax7.set_yticks(minor_ticks_y, minor=True)

# Set the tick labels font
for label in (ax7.get_xticklabels() + ax7.get_yticklabels()):
#    label.set_fontname('Arial')
    label.set_fontsize(12)


"""
########## SERPENS, C34S 3-2 (x 3), center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
ax7.plot(v_c34s32_p7, 3*(Tmb_c34s32_p7) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
ax7.plot(v_cs32_p7, Tmb_cs32_p7 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 145.5 -78.8, range 131.6 159.4 -92.7 -64.9 ##########
"""
##ax7.plot(v_h13cn21_p7, Tmb_h13cn21_p7 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
ax7.plot(v_h13cn10_p7, 5*(Tmb_h13cn10_p7) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
ax7.plot(v_hcn10_p7, Tmb_hcn10_p7 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 145.5 -78.8, range: 131.6 159.4 -92.7 -64.9 ##########
"""
ax7.plot(v_cn10_p7, Tmb_cn10_p7, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1, linestyle = '-')


ax7.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax7.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax7.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data'
#)
ax7.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax7.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax7.annotate(r'$\mathrm{CN\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax7.annotate(r'$\mathrm{SMM9}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')



# the upper and lower axis limits on a RIGHT GRAPH
ax7.set_xlim([-90.0, 40.0])
ax7.set_ylim([-0.5, 22.5])




# close and save file
savefig(psname, format = 'eps', bbox_inches = 'tight') 
clf()
