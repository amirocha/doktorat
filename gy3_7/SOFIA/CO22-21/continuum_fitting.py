'''Baseline fitting + find continuum'''
import pyspeckit
from astropy.io import fits
import numpy as np


def read_data(file_name):

	file1 = open(file_name, 'r')
	data = file1.readlines()
	file1.close()

	return data

def exclude_ends(data, number):

	new_data = []
	for i in range(number, len(data)-number):  
		xaxis = data[i].split()[0]
		yaxis = data[i].split()[1]
		new_line = f'{xaxis}\t{yaxis}\n'
		new_data.append(new_line)

	return new_data

def write_to_file(data, file_end_name):

	file1 = open(file_end_name, 'w')
	file1.writelines(data)
	file1.close()

def fit_baseline(spectrum, pixel1, pixel2, line_pixel, line_begin, line_end):

	sp = pyspeckit.Spectrum(spectrum)
	sp.plotter() 
	sp.baseline(interactive=False, subtract=False, save=True, exclude = (line_begin, line_end), highlight_fitregion = True)
	sp.plotter.savefig('./baselines/'+str(pixel1)+'__'+str(pixel2)+'_baseline_fit.png')
	model = (sp.baseline.baselinepars[0], sp.baseline.baselinepars[1])

	return model	

def find_continuum(model, line):

	continuum = model[0] * line + model[1]
	if continuum < 0:
		continuum = 0

	return continuum

def write_continuum_to_file(continuum, ra, dec, i):
	
	line = f'{i}\t{ra}\t{dec}\t{continuum}\n'
	file1 = open('CO22-21_continuum.txt', 'a')
	file1.writelines(line)
	file1.close()

def main():  
	hdl = fits.open('../data/F0636_FI_IFS_0701572_BLU_WXY_00629-00877.fits', memmap=None, ignore_blank=True)
	flux = hdl['FLUX'].data  #cube: spectra(len=53) -> X(len=17) -> Y(len=17)
	wavelength = hdl['WAVELENGTH'].data #list(len=53)
	X = hdl['X'].data #list(len=17)
	Y = hdl['Y'].data #list(len=17)

	line = 118.581
	line_pixel = 118.58643313852755
	array = np.where(wavelength == 118.58643313852755)
	index = int(array[0])
	step = 4
	ends = 10
	line_begin = wavelength[index-step]
	line_end = wavelength[index+step]
	counter = 0

	for i in range(len(X)):
		for j in range(len(Y)):
			pixel_spectrum = []
			pixel_file = 'pixel.txt' #+str(X[i])+'_'+str(Y[j])
			for k in range(ends, len(wavelength)-ends):
				if np.isnan(flux[k][i][j]) == False:
					new_line = f'{wavelength[k]}\t{flux[k][i][j]}\n'
					pixel_spectrum.append(new_line)	
			if len(pixel_spectrum) > 2:	
				write_to_file(pixel_spectrum, pixel_file)
				model = fit_baseline(pixel_file, X[i], Y[j], line_pixel, line_begin, line_end)
				continuum = find_continuum(model, line)
				write_continuum_to_file(continuum, X[i], Y[j], counter)
				counter +=1
	

if __name__ == '__main__': 
	main()

