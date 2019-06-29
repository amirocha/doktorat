import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

data = np.genfromtxt('serpens_cn10_smm1_cut.txt')

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

errfunc3 = lambda p, x, y: (three_gaussians(x, *p) - y)**2
errfunc2 = lambda p, x, y: (two_gaussians(x, *p) - y)**2
errfunc4 = lambda p, x, y: (four_gaussians(x, *p) - y)**2

guess3 = [0.5, 6.8, 0.04, 0.9, 7.8, 1, 0.7, 9.3, 0.8, 0.2]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there // h1, c1, w1, h2, c2, w2, h3, c3, w3, offset
guess2 = [0.9, 7.8, 1, 0.7, 9.5, 1, 0.2]  # I removed the peak I'm not too sure about
guess4 = [0.5, 6.8, 0.04, 0.9, 7.8, 1, 0.67, 9.5, 0.3, 5.9, 9.9, 0.3, 0.2]
optim3, success = optimize.leastsq(errfunc3, guess3[:], args=(data[:,0], data[:,1]))
optim2, success = optimize.leastsq(errfunc2, guess2[:], args=(data[:,0], data[:,1]))
optim4, success = optimize.leastsq(errfunc4, guess4[:], args=(data[:,0], data[:,1]))

plt.plot(data[:,0], data[:,1], lw=1, c='g', label='data')
plt.plot(data[:,0], three_gaussians(data[:,0], *optim3),
    lw=1, c='b', label='fit of 3 Gaussians')
#plt.plot(data[:,0], two_gaussians(data[:,0], *optim2), lw=1, c='r', ls='--', label='fit of 2 Gaussians')
plt.plot(data[:,0], four_gaussians(data[:,0], *optim4), lw=1, c='m', ls='-', label='fit of 4 Gaussians')
plt.legend(loc='best')
plt.savefig('test.png')

err3 = np.sqrt(errfunc3(optim3, data[:,0], data[:,1])).sum()
err2 = np.sqrt(errfunc2(optim2, data[:,0], data[:,1])).sum()
err4 = np.sqrt(errfunc4(optim4, data[:,0], data[:,1])).sum()
print('Residual error when fitting 4 Gaussians: {}\n'
	'Residual error when fitting 3 Gaussians: {}\n'
    'Residual error when fitting 2 Gaussians: {}'.format(err4, err3, err2))


