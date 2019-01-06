'''Fits multigassian funtion to hiperfine splitted lines'''
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def read_data(molecule,i):
	data=np.loadtxt('./spectra/smm1_'+molecule+'_'+str(i)+'.txt')
	velocity = data[:,0]	#copy the first column (velocities) without changing the original data
	flux = data[:,1]  #copy the second column
	return (velocity,flux)	

def gaussian(x, height, center, width, offset=0.):
	return height*np.exp(-(x - center)**2/(2*width**2)) + offset

def three_gaussians(x, h1, c1, w1, h2, c2, w2, h3, c3, w3, offset=0.):
	return (gaussian(x, h1, c1, w1, offset=0) + gaussian(x, h2, c2, w2, offset=0) + gaussian(x, h3, c3, w3, offset=0) + 1)

def four_gaussians(x, h1, c1, w1, h2, c2, w2, h3, c3, w3, h4, c4, w4, offset=0.):
	return (gaussian(x, h1, c1, w1, offset=0) + gaussian(x, h2, c2, w2, offset=0) + gaussian(x, h3, c3, w3, offset=0) + gaussian(x, h4, c4, w4, offset=0) + 1)

def two_gaussians(x, h1, c1, w1, h2, c2, w2, offset=0.):
	return three_gaussians(x, h1, c1, w1, h2, c2, w2, 0,0,1, offset)

def calculate_errors(velocity, flux):
	errfunc3 = lambda p, x, y: (three_gaussians(x, *p) - y)**2
	errfunc2 = lambda p, x, y: (two_gaussians(x, *p) - y)**2
	errfunc4 = lambda p, x, y: (four_gaussians(x, *p) - y)**2

	guess3 = [-0.2, -120, 20, -0.2, -80, 20, -0.2, -80, 20, 1]  #guess the parameters
	guess2 = [-0.2, -80, 20, -0.2, -80, 20, 1]
	guess4 = [-0.2, -120, 20, -0.2, -120, 20, -0.2, -120, 20, -0.2, -80, 20, 1]
	optim3, success = optimize.leastsq(errfunc3, guess3[:], args=(velocity, flux))
	optim2, success = optimize.leastsq(errfunc2, guess2[:], args=(velocity, flux))
	optim4, success = optimize.leastsq(errfunc4, guess4[:], args=(velocity, flux))
	optim3 #parameters of individual gaussians

	err3 = np.sqrt(errfunc3(optim3, velocity, flux)).sum()
	err2 = np.sqrt(errfunc2(optim2, velocity, flux)).sum()
	err4 = np.sqrt(errfunc4(optim4, velocity, flux)).sum()
	print('Residual error when fitting 2 Gaussians: {}\n' 'Residual error when fitting 3 Gaussians: {}\n' 'Residual error when fitting 4 Gaussians: {}\n'.format(err2,err3,err4))

	return optim3, optim4

def draw_figure(velocity, flux, optim3, optim4):
	fig, ax = plt.subplots(2, 1, sharex=True, figsize=[14,7])
	ax = plt.subplot(1, 2, 1)
	plt.plot(velocity, flux, color='k', label='measurement')
	plt.plot(velocity, three_gaussians(velocity, *optim3), lw=2, ls='--', color='m', label='fit of 3 Gaussians')
	for i in range(3):
		plt.plot(velocity, gaussian(velocity, *optim3[i*3:3+i*3], offset=optim3[-1]), color=100+i)
	plt.legend(loc='best')
	plt.text(-70, 10.1, (r'$^{12}$CO J=6-5'), fontsize=18, fontdict={'color': 'k', 'family':'serif'})
	ax.set_xlim([-75.0, 25.00]) # the upper and lower axis limits on x axis
	
	
	ax = plt.subplot(1, 2, 2)
	plt.plot(velocity, flux, color='k', label='measurement')
	plt.plot(velocity, four_gaussians(velocity, *optim4), lw=2, ls='--', color='m', label='fit of 4 Gaussians')
	for i in range(4):
		plt.plot(velocity, gaussian(velocity, *optim4[i*3:3+i*3], offset=optim4[-1]), color='r')
	plt.text(-70, 10.1, (r'$^{12}$CO J=6-5'), fontsize=18, fontdict={'color': 'k', 'family':'serif'})
	plt.legend(loc='best')
	ax.set_xlim([-75.0, 25.00]) # the upper and lower axis limits on x axis
	plt.savefig("multigauss.png",bbox_inches="tight")
	plt.close('all') 

def main():
	molecule = 'co65' #change the molecule 
	for i in range(34):
		if i not in [0,1,4,9,10,15,20,25,26,30,31,34]:   #change the number of itterations (spectra) + conditions
			data = read_data(molecule,5)
	optim=calculate_errors(data[0],data[1])
	draw_figure(data[0],data[1],optim[0],optim[1])


if __name__ == '__main__': 
	main()

