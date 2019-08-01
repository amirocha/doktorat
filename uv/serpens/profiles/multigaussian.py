import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.integrate import quad



def gaussian(x, height, center, width, offset):
    return height*np.exp(-(x - center)**2/(2*width**2)) + offset   #center = mean // offset - vertical offset

def three_gaussians(x, h1, c1, w1, h2, c2, w2, h3, c3, w3, offset):
    return (gaussian(x, h1, c1, w1, offset=0) +
        gaussian(x, h2, c2, w2, offset=0) +
        gaussian(x, h3, c3, w3, offset=0) + offset)

def four_gaussians(x, h1, c1, w1, h2, c2, w2, h3, c3, w3, h4, c4, w4, offset):
    return (gaussian(x, h1, c1, w1, offset=0) +
        gaussian(x, h2, c2, w2, offset=0) +
        gaussian(x, h3, c3, w3, offset=0) + gaussian(x, h4, c4, w4, offset=0) + offset)

def two_gaussians(x, h1, c1, w1, h2, c2, w2, offset):
    return three_gaussians(x, h1, c1, w1, h2, c2, w2, 0,0,1, offset)

def write_data(end_filename, data):
	file = open(end_filename,'a')
	file.writelines(data)
	file.close()

for pos in [5,8]:
	data = np.genfromtxt('serpens_cn10_smm'+str(pos)+'_comp2.txt')

	errfunc3 = lambda p, x, y: (three_gaussians(x, *p) - y)**2
	errfunc2 = lambda p, x, y: (two_gaussians(x, *p) - y)**2
	errfunc4 = lambda p, x, y: (four_gaussians(x, *p) - y)**2
	errfunc1 = lambda p, x, y: (gaussian(x, *p) - y)**2

	guess3 = [0.7, 15.5, 2, 0.4, 16.5, 1, 0.3, 15, 0.8, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [0.7, 15.5, 2, 0.4, 16.5, 1, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [0.7, 15.5, 2, 0.4, 16.5, 1, 0.3, 15, 0.3, 0.3, 17, 0.3, 0.2]
	guess1 = [1.0, 15.5, 1.5, 0.2]
	optim1, success = optimize.leastsq(errfunc1, guess1[:], args=(data[:,0], data[:,1]))
	optim3, success = optimize.leastsq(errfunc3, guess3[:], args=(data[:,0], data[:,1]))
	optim2, success = optimize.leastsq(errfunc2, guess2[:], args=(data[:,0], data[:,1]))
	optim4, success = optimize.leastsq(errfunc4, guess4[:], args=(data[:,0], data[:,1]))

	plt.plot(data[:,0], data[:,1], lw=1, c='g', label='data')
	plt.plot(data[:,0], gaussian(data[:,0], *optim1), lw=1, c='m', ls='-', label='fit of 1 Gaussian')
	plt.plot(data[:,0], three_gaussians(data[:,0], *optim3), lw=1, c='b', label='fit of 3 Gaussians')
	plt.plot(data[:,0], two_gaussians(data[:,0], *optim2), lw=1, c='r', ls='--', label='fit of 2 Gaussians')
	plt.plot(data[:,0], four_gaussians(data[:,0], *optim4), lw=1, c='c', ls='-', label='fit of 4 Gaussians')
	plt.legend(loc='best')
	plt.savefig('serpens_cn10_smm'+str(pos)+'_1comp.png')
	plt.clf()

	err3 = np.sqrt(errfunc3(optim3, data[:,0], data[:,1])).sum()
	err2 = np.sqrt(errfunc2(optim2, data[:,0], data[:,1])).sum()
	err4 = np.sqrt(errfunc4(optim4, data[:,0], data[:,1])).sum()
	err1 = np.sqrt(errfunc1(optim1, data[:,0], data[:,1])).sum()

	flux_3gauss, err_3gauss = quad(lambda x: optim3[0]*np.exp(-(x - optim3[1])**2/(2*optim3[2]**2)) + optim3[3]*np.exp(-(x - optim3[4])**2/(2*optim3[5]**2) + optim3[6]*np.exp(-(x - optim3[7])**2/(2*optim3[8]**2))) + optim3[9], 13,18)	
	flux_4gauss, err_4gauss = quad(lambda x: optim4[0]*np.exp(-(x - optim4[1])**2/(2*optim4[2]**2)) + optim4[3]*np.exp(-(x - optim4[4])**2/(2*optim4[5]**2)) + optim4[6]*np.exp(-(x - optim4[7])**2/(2*optim4[8]**2)) + optim4[9]*np.exp(-(x - optim4[10])**2/(2*optim4[11]**2)) + optim4[12], 13,18)
	flux_2gauss, err_2gauss = quad(lambda x: optim2[0]*np.exp(-(x - optim2[1])**2/(2*optim2[2]**2)) + optim2[3]*np.exp(-(x - optim2[4])**2/(2*optim2[5]**2)) + optim2[6],13,18)
	flux_1gauss, err_1gauss = quad(lambda x: optim1[0]*np.exp(-(x - optim1[1])**2/(2*optim1[2]**2)) + optim2[3], 13,18)
	
	results = [f'SMM{pos} cn10 1comp\n \t\t1Gauss:{flux_1gauss:5.3} Err:{err1:5.3}\n \t\t2Gauss:{flux_2gauss:5.3} Err:{err2:5.3}\n \t\t3Gauss:{flux_3gauss:5.3} Err:{err3:5.3}\n \t\t4Gauss:{flux_4gauss:5.3} Err:{err4:5.3} \n']
	write_data('serpens_fluxes.txt', results)
	#print('Residual error when fitting 4 Gaussians: {}\n' 'Residual error when fitting 3 Gaussians: {}\n' 'Residual error when fitting 2 Gaussians: {}'.format(err4, err3, err2))

'''
#guesses:
CN1-0 comp 1:
guess3 = [0.9, 15.5, 2, 0.8, 15, 1, 0.5, 16, 0.8, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [0.9, 15.5, 2, 0.8, 15, 1, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [0.9, 15.5, 2, 0.8, 15, 1, 0.5, 16, 0.3, 0.3, 17, 0.3, 0.2]
	guess1 = [1.0, 15.5, 1.5, 0.2]
integration: 13 18

CN1-0 comp 2:
guess3 = [0.5, 6.8, 0.04, 0.9, 7.8, 1, 0.7, 9.3, 0.8, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [0.9, 7.8, 1, 0.7, 9.5, 1, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [0.5, 6.8, 0.04, 0.9, 7.8, 1, 0.57, 9.5, 0.3, 5.9, 9.9, 0.3, 0.2]
integration: 5 13

CN1-0 comp3:
guess3 = [0.9, -15, 1.5, 0.7, -15, 0.5, 0.7, -15, 0.5, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [0.9, -15, 1.5, 0.7, -15, 0.5, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [0.5, 6.8, 0.04, 0.9, 7.8, 1, 0.57, 9.5, 0.3, 5.9, 9.9, 0.3, 0.2]
	guess1 = [0.9, -15, 1.5, 0.2]
integration: -20 -10

CN1-0 comp4:
guess3 = [1.0, -38, 1.5, 1.2, -41, 1.5, 0.9, -38, 1.5, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [1.0, -38, 1.5, 1.2, -41, 1.5, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [1.5, 6.8, 0.04, 0.9, 7.8, 1, 0.57, 9.5, 0.3, 5.9, 9.9, 0.3, 0.2]
	guess1 = [1.0, -38, 1.5, 0.2]
integration: -45 -30


HCN 1-0 comp1:
guess3 = [0.9, 11, 2, 0.7, 11, 1, 0.3, 13.5, 0.5, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [0.9, 11, 2, 0.7, 11, 1, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [1.5, 6.8, 0.04, 0.9, 7.8, 1, 0.57, 9.5, 0.3, 5.9, 9.9, 0.3, 0.2]
	guess1 = [0.9, 11, 2, 0.2]
integration: 10 15

HCN 1-0 comp3:
guess3 = [0.7, 0, 2, 0.3, 1, 1, 0.4, -0.5, 0.5, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [0.7, 0, 2, 0.3, 1, 1, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [0.7, 0, 2, 0.3, 1, 1, 0.4, -0.5, 0.5, 0.2, 1.5, 0.3, 0.2]
	guess1 = [0.7, 0, 2, 0.2]
integration: -3 3

CS 3-2:
guess3 = [2.7, 10, 2, 2.2, 7.5, 2, 1, 6, 1, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [2.7, 10, 2, 2.2, 7.5, 2, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [2.7, 10, 2, 2.2, 7.5, 2, 1, 6, 0.5, 1.5, 7, 0.3, 0.2]
	guess1 = [2.7, 10, 2, 0.2]
integration: 5 14

C34S 3-2:
guess3 = [0.7, 9, 2, 0.5, 8, 2, 0.2, 10, 1, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [0.7, 9, 2, 0.5, 8, 2, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [0.7, 9, 2, 0.5, 8, 2, 0.2, 10, 0.5, 1.5, 7, 0.3, 0.2]
	guess1 = [0.7, 9, 2, 0.2]
integration: 6 10

H13CN 1-0 comp2:
guess3 = [0.4, 19.5, 1, 0.25, 20.5, 1, 0.17, 20, 1, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
	guess2 = [0.4, 19.5, 1, 0.25, 20.5, 1, 0.2]  # I removed the peak I'm not too sure about
	guess4 = [0.4, 19.5, 1, 0.25, 20.5, 1, 0.17, 20, 1 ,0.2, 19, 1, 0.2]
	guess1 = [0.4, 19.5, 1, 0.2]
integration 18 22
'''
