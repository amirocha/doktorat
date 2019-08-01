'''
DESCRIPTION: This script displays the resampled profiles (0.5 km/s)
DESCRIPTION: of diff. molecules for 14 diff. positions in SERPENS

The averaged region is consistent with HCN 1-0 beam size (27.8"), 
because it's the biggest for this molecule. We used the same 
beam size for other molecules.
'''

#!/usr/bin/python3.3

# name the output file
psname = 'serpens_8-14_spectra_vel_resam.eps'

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



""" EIGHTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
v_c34s32_p8, Tmb_c34s32_p8 = loadtxt('./serpens_c34s32_smm10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
v_cs32_p8, Tmb_cs32_p8 = loadtxt('./serpens_cs32_smm10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
#v_h13cn21_p8, Tmb_h13cn21_p8 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_122.473_150.273_-83.292_-55.492_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
v_h13cn10_p8, Tmb_h13cn10_p8 = loadtxt('./serpens_h13cn10_smm10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
v_hcn10_p8, Tmb_hcn10_p8 = loadtxt('./serpens_hcn10_smm10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
v_cn10_p8, Tmb_cn10_p8 = loadtxt('./serpens_cn10_smm10.txt', usecols=(0, 1), unpack=True, skiprows=1)



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
EIGHTH PANEL - CREATE A PLOT
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
########## SERPENS, C34S 3-2 (x 3), center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
ax1.plot(v_c34s32_p8, 3*(Tmb_c34s32_p8) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
ax1.plot(v_cs32_p8, Tmb_cs32_p8 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
#ax1.plot(v_h13cn21_p8, Tmb_h13cn21_p8 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
ax1.plot(v_h13cn10_p8, 5*(Tmb_h13cn10_p8) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
ax1.plot(v_hcn10_p8, Tmb_hcn10_p8 + 4, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 136.373 -69.392, range: 122.473 150.273 -83.292 -55.492 ##########
"""
ax1.plot(v_cn10_p8, Tmb_cn10_p8, color = 'black', linewidth=1.0, linestyle = '-')
ax1.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')


ax1.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax1.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax1.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax1.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax1.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax1.annotate(r'$\mathrm{CN(F1)\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax1.annotate(r'$\mathrm{SMM10}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')



# the upper and lower axis limits on a LEFT GRAPH
ax1.set_xlim([-90.0, 40.0])
ax1.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" NINTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
v_c34s32_p9, Tmb_c34s32_p9 = loadtxt('./serpens_c34s32_smm12.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
v_cs32_p9, Tmb_cs32_p9 = loadtxt('./serpens_cs32_smm12.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
#v_h13cn21_p9, Tmb_h13cn21_p9 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_109.1_136.9_-89.1_-61.3_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
v_h13cn10_p9, Tmb_h13cn10_p9 = loadtxt('./serpens_h13cn10_smm12.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
v_hcn10_p9, Tmb_hcn10_p9 = loadtxt('./serpens_hcn10_smm12.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
v_cn10_p9, Tmb_cn10_p9 = loadtxt('./serpens_cn10_smm12.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
NINTH PANEL - CREATE A PLOT
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
########## SERPENS, C34S 3-2 (x 3), center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
ax2.plot(v_c34s32_p9, 3*(Tmb_c34s32_p9) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
ax2.plot(v_cs32_p9, Tmb_cs32_p9 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
#ax2.plot(v_h13cn21_p9, Tmb_h13cn21_p9 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
ax2.plot(v_h13cn10_p9, 5*(Tmb_h13cn10_p9) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
ax2.plot(v_hcn10_p9, Tmb_hcn10_p9 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 123 -75.2, range: 109.1 136.9 -89.1 -61.3 ##########
"""
ax2.plot(v_cn10_p9, Tmb_cn10_p9, color = 'black', linewidth=1.0, linestyle = '-')
ax2.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')


ax2.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax2.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax2.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax2.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax2.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data'
)
ax2.annotate(r'$\mathrm{CN(F1)\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data'
)
ax2.annotate(r'$\mathrm{SMM12}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data'
)



# the upper and lower axis limits on a RIGHT GRAPH
ax2.set_xlim([-90.0, 40.0])
ax2.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" TENTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
v_c34s32_p10, Tmb_c34s32_p10 = loadtxt('./serpens_c34s32_pos1.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
v_cs32_p10, Tmb_cs32_p10 = loadtxt('./serpens_pos1_cs32.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
#v_h13cn21_p10, Tmb_h13cn21_p10 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_-14.5_13.3_-12.5_15.3_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
v_h13cn10_p10, Tmb_h13cn10_p10 = loadtxt('./serpens_pos1_h13cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
v_hcn10_p10, Tmb_hcn10_p10 = loadtxt('./serpens_pos1_hcn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
v_cn10_p10, Tmb_cn10_p10 = loadtxt('./serpens_pos1_cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
TENTH PANEL - CREATE A PLOT
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
########## SERPENS, C34S 3-2 (x 3), center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
ax3.plot(v_c34s32_p10, 3*(Tmb_c34s32_p10) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
ax3.plot(v_cs32_p10, Tmb_cs32_p10 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
#ax3.plot(v_h13cn21_p10, Tmb_h13cn21_p10 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
ax3.plot(v_h13cn10_p10, 5*(Tmb_h13cn10_p10) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
ax3.plot(v_hcn10_p10, Tmb_hcn10_p10 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: -0.6 1.4, range: -14.5 13.3 -12.5 15.3 ##########
"""
ax3.plot(v_cn10_p10, Tmb_cn10_p10, color = 'black', linewidth=1.0, linestyle = '-')
ax3.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')


ax3.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax3.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax3.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax3.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax3.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data'
)
ax3.annotate(r'$\mathrm{CN(F1)\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data'
)
ax3.annotate(r'$\mathrm{Outflow1}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data'
)


# the upper and lower axis limits on a RIGHT GRAPH
ax3.set_xlim([-90.0, 40.0])
ax3.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" ELEVENTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
v_c34s32_p11, Tmb_c34s32_p11 = loadtxt('./serpens_c34s32_pos2.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
v_cs32_p11, Tmb_cs32_p11 = loadtxt('./serpens_pos2_cs32.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
#v_h13cn21_p11, Tmb_h13cn21_p11 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_23.6_51.4_14.6_42.4_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
v_h13cn10_p11, Tmb_h13cn10_p11 = loadtxt('./serpens_pos2_h13cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
v_hcn10_p11, Tmb_hcn10_p11 = loadtxt('./serpens_pos2_hcn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
v_cn10_p11, Tmb_cn10_p11 = loadtxt('./serpens_pos2_cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
ELEVENTH PANEL - CREATE A PLOT
"""
ax4.set_xlabel(r'$\mathrm{V_{LSR}\;[km/s]}$', fontsize = 14)


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
########## SERPENS, C34S 3-2 (x 3), center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
ax4.plot(v_c34s32_p11, 3*(Tmb_c34s32_p11) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
ax4.plot(v_cs32_p11, Tmb_cs32_p11 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
#ax4.plot(v_h13cn21_p11, Tmb_h13cn21_p11 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
ax4.plot(v_h13cn10_p11, 5*(Tmb_h13cn10_p11) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
ax4.plot(v_hcn10_p11, Tmb_hcn10_p11 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 37.5 28.5, range: 23.6 51.4 14.6 42.4 ##########
"""
ax4.plot(v_cn10_p11, Tmb_cn10_p11, color = 'black', linewidth=1.0, linestyle = '-')
ax4.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')


ax4.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax4.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax4.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax4.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax4.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data'
)
ax4.annotate(r'$\mathrm{CN(F1)\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data'
)
ax4.annotate(r'$\mathrm{Outflow2}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data'
)


# the upper and lower axis limits on a RIGHT GRAPH
ax4.set_xlim([-90.0, 40.0])
ax4.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" TWELFTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
v_c34s32_p12, Tmb_c34s32_p12 = loadtxt('./serpens_c34s32_pos3.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
v_cs32_p12, Tmb_cs32_p12 = loadtxt('./serpens_pos3_cs32.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
#v_h13cn21_p12, Tmb_h13cn21_p12 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_13.1_40.9_63.9_91.7_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
v_h13cn10_p12, Tmb_h13cn10_p12 = loadtxt('./serpens_pos3_h13cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
v_hcn10_p12, Tmb_hcn10_p12 = loadtxt('./serpens_pos3_hcn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
v_cn10_p12, Tmb_cn10_p12 = loadtxt('./serpens_pos3_cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
TWELFTH  PANEL - CREATE A PLOT
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
########## SERPENS, C34S 3-2 (x 3), center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
ax5.plot(v_c34s32_p12, 3*(Tmb_c34s32_p12) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
ax5.plot(v_cs32_p12, Tmb_cs32_p12 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
#ax5.plot(v_h13cn21_p12, Tmb_h13cn21_p12 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
ax5.plot(v_h13cn10_p12, 5*(Tmb_h13cn10_p12) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
ax5.plot(v_hcn10_p12, Tmb_hcn10_p12 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: 27 77.8, range: 13.1 40.9 63.9 91.7 ##########
"""
ax5.plot(v_cn10_p12, Tmb_cn10_p12, color = 'black', linewidth=1.0, linestyle = '-')
ax5.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')


ax5.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax5.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax5.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax5.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax5.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax5.annotate(r'$\mathrm{CN(F1)\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax5.annotate(r'$\mathrm{Outflow3}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')


# the upper and lower axis limits on a RIGHT GRAPH
ax5.set_xlim([-90.0, 40.0])
ax5.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" THIRTEENTH PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
v_c34s32_p13, Tmb_c34s32_p13 = loadtxt('./serpens_c34s32_pos4.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
v_cs32_p13, Tmb_cs32_p13 = loadtxt('./serpens_pos4_cs32.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
#v_h13cn21_p13, Tmb_h13cn21_p13 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_-36.85_-9.05_67.1_94.9_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
v_h13cn10_p13, Tmb_h13cn10_p13 = loadtxt('./serpens_pos4_h13cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
v_hcn10_p13, Tmb_hcn10_p13 = loadtxt('./serpens_pos4_hcn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
v_cn10_p13, Tmb_cn10_p13 = loadtxt('./serpens_pos4_cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
THIRTEENTH PANEL - CREATE A PLOT
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
########## SERPENS, C34S 3-2 (x 3), center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
ax6.plot(v_c34s32_p13, 3*(Tmb_c34s32_p13) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
ax6.plot(v_cs32_p13, Tmb_cs32_p13 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
#ax6.plot(v_h13cn21_p13, Tmb_h13cn21_p13 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
ax6.plot(v_h13cn10_p13, 5*(Tmb_h13cn10_p13) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
ax6.plot(v_hcn10_p13, Tmb_hcn10_p13 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: -22.95 81, range: -36.85 -9.05 67.1 94.9 ##########
"""
ax6.plot(v_cn10_p13, Tmb_cn10_p13, color = 'black', linewidth=1.0, linestyle = '-')
ax6.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')


ax6.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax6.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax6.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax6.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax6.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data'
)
ax6.annotate(r'$\mathrm{CN(F1)\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data'
)
ax6.annotate(r'$\mathrm{Outflow4}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data'
)


# the upper and lower axis limits on a RIGHT GRAPH
ax6.set_xlim([-90.0, 40.0])
ax6.set_ylim([-0.5, 22.5])





"""
***************************************************************
***************************************************************
***************************************************************
"""





""" FOURTEEN PANEL - READ INPUT DATA
########## SERPENS, C34S 3-2, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
v_c34s32_p14, Tmb_c34s32_p14 = loadtxt('./serpens_c34s32_pos5.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CS 3-2, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
v_cs32_p14, Tmb_cs32_p14 = loadtxt('./serpens_pos5_cs32.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 2-1, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
#v_h13cn21_p14, Tmb_h13cn21_p14 = loadtxt('/Users/gladki/WORK/IRAM_class/reduction_marcin_w_conv/serpens/ave_profiles_plots/h13cn21_ran_-39.214_-11.414_81.9_109.7_resam_vel_spec.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, H13CN 1-0, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
v_h13cn10_p14, Tmb_h13cn10_p14 = loadtxt('./serpens_pos5_h13cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, HCN 1-0, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
v_hcn10_p14, Tmb_hcn10_p14 = loadtxt('./serpens_pos5_hcn10.txt', usecols=(0, 1), unpack=True, skiprows=1)


"""
########## SERPENS, CN 1-0, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
v_cn10_p14, Tmb_cn10_p14 = loadtxt('./serpens_pos5_cn10.txt', usecols=(0, 1), unpack=True, skiprows=1)





"""
FOURTEEN PANEL - CREATE A PLOT
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
########## SERPENS, C34S 3-2 (x 3), center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
ax7.plot(v_c34s32_p14, 3*(Tmb_c34s32_p14) + 19.0, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=19, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CS 3-2, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
ax7.plot(v_cs32_p14, Tmb_cs32_p14 + 14.0, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=14, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, H13CN 2-1, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
#ax7.plot(v_h13cn21_p14, Tmb_h13cn21_p14 + 12.0, color = 'black', linewidth=1.0, linestyle = '-')


"""
########## SERPENS, H13CN 1-0 (x 5), center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
ax7.plot(v_h13cn10_p14, 5*(Tmb_h13cn10_p14) + 10.0, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=10, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, HCN 1-0, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
ax7.plot(v_hcn10_p14, Tmb_hcn10_p14 + 4.0, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=4, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')

"""
########## SERPENS, CN 1-0, center: -25.314 95.8, range: -39.214 -11.414 81.9 109.7 ##########
"""
ax7.plot(v_cn10_p14, Tmb_cn10_p14, color = 'black', linewidth=1.0, linestyle = '-')
ax7.axhline(y=0, xmin = -90.0, xmax = 40.0, color = 'green', linewidth=1.0, linestyle = '-')


ax7.annotate(r'$\mathrm{C^{34}S\;\;3-2\;(\times3)}$', fontsize=12, xy=(-85.0, 20.0), textcoords='data')
ax7.annotate(r'$\mathrm{CS\;\;3-2}$', fontsize=12, xy=(-85.0, 14.4), textcoords='data')
#ax7.annotate(r'$\mathrm{H^{13}CN\;\;2-1}$', fontsize=12, xy=(-85.0, 12.5), textcoords='data')
ax7.annotate(r'$\mathrm{H^{13}CN\;\;1-0\;(\times5)}$', fontsize=12, xy=(-85.0, 12.0), textcoords='data')
ax7.annotate(r'$\mathrm{HCN\;\;1-0}$', fontsize=12, xy=(-85.0, 4.5), textcoords='data')
ax7.annotate(r'$\mathrm{CN(F1)\;\;1-0}$', fontsize=12, xy=(-85.0, 1.7), textcoords='data')
ax7.annotate(r'$\mathrm{Outflow5}$', color='blue', fontsize=18, xy=(-50.0, 21.5), textcoords='data')


# the upper and lower axis limits on a RIGHT GRAPH
ax7.set_xlim([-90.0, 40.0])
ax7.set_ylim([-0.5, 22.5])



# close and save file
savefig(psname, format = 'eps', bbox_inches = 'tight') 
clf()
