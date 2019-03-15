from greybody import GreyBody
import numpy as np
import matplotlib.pyplot as plt
import math as m

def greybody(D, beta, kappa350, wave, T, M):
    nu = c / (wave*1e-6)                                    # Hz
    nu350 = 230*10e9                                      # Hz
    kappa = kappa350 * (nu/nu350)**beta                     # m2/kg
    Bnu = 2*h*nu**3/ c**2 / (np.exp((h*nu)/(k*T)) - 1)      # W/m2/Hz
    flux = M*Msun * kappa * Bnu / (D*pc)**2                 # W/m2/Hz
    return flux * 1e26    

# universal constants and units
c = 2.99792458e8        # m/s
h = 6.62606957e-34      # J s
k = 1.3806488e-23       # J/K
pc = 3.08567758e16      # m
Msun = 1.9891e30        # kg
Lsun = 3.8281e26        # W

# specific parameters
D = 436 #pc
beta = 2.

#Herschel photometry
#SMM9
lambdav = (70, 160, 250, 350, 500) #microns
flux = (14.69, 63, 30, 17.8, 19.3) #Jy (tot)
sigma = (0.24, 1.8, 2.1, 1.8, 1.4) #errors
a = 20.4*((2*m.pi)/(360*60*60))  #beam's major axis [rad]
b = 18.2*((2*m.pi)/(360*60*60))  #beam's minor axis [rad]

c = 2.99792458e8   #m/s
nu = [(c/(i/1000000.))/1e9 for i in lambdav]  
kappa = 0.1*pow((230/1000.),beta) #from Könyves+2010 [cm^2/g]

g = GreyBody(D=D, beta=beta, kappa350=kappa)

results = g.fit(lambdav, fluxv=flux, sigmav=sigma) #temperature T (K) and the dust mass M (Msun)

print(results)

#bolometric luminosity

beam = m.pi*a*b*pow(D*pc,2)

x = [i for i in range(1,600)] #microns
y = [] #Jy
X=[] #Hz
integral = 0.
for i in x:
	elem = greybody(D, beta, kappa, i, results[0], results[1])
	y.append(elem)
	X.append(c/(i/1e6)) #Hz


for i in range(len(x)-1):
	integral+=(1e-26*y[i]*(abs(X[i+1]-X[i]))*beam)/Lsun # W

print(integral) #bolometric luminosity

#plot
fig=plt.figure()
plt.title("SED SMM9", fontsize=14)
plt.ylabel("Flux [Jy]", fontsize=12)
plt.xlabel("Wavelength [microns]", fontsize=12)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(400, 60, 'T='+str(round(results[0]))+' K', fontsize=10, verticalalignment='top', bbox=props)
plt.plot(x, y, 'k-', linewidth=0.6, linestyle='steps')
plt.plot(lambdav, flux, 'ro', linewidth=1)

plt.savefig('sed_smm9.png')
plt.close()
