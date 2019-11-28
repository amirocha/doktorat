#!/bin/bash

for i in 5.000D+01 1.000D+02 1.500D+02 2.000D+02 2.500D+02 3.000D+02
do
  for j in -4.50D+00 -4.00D+00 -3.50D+00 -3.00D+00 -2.50D+00 -2.00D+00 -1.50D+00 -1.00D+00 -0.50D+00 0.000D+00 0.500D+00 1.000D+00 1.500D+00 2.000D+00 2.500D+00    
  do
    echo "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c	input_parameter.dat
c	May 2006 Wakelam Valentine
c	input file of the parameters
c	Please respect the format
c	If you are running the uncertainties, the gas temperature and density 
c	will not be read from this file
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
N			/ Do you want to run in the uncertainty mode ? Y or N
1.000D+05		/ H tot Density (cm-3) = n(H)+2*n(H2)
"$i"		/ Temperature (K)
"$j"		/ Visual extinction
1.063D+07		/ Time (in timeres.dat) when you want the output.dat to be written
1.300D-17		/ Cosmic-ray ionization rate (s-1)
1.000D-02       	/ Dust to gas mass ratio (usually 0.01)
1.000D-05     		/ Dust grain radius (in cm)
3.000D+00		/ grain density (in g cm-3)" > input_parameter.dat
    gfortran opkd*.f nahoon_1dx.f90 -o nahoon_1d
    chmod a+x nahoon_1d
    ./nahoon_1d 
    #python3 plot_concentrations.py
    mv output.dat output$i-$j.dat 
    mv plot.dat plot$i-$j.dat 
    mv verif.dat verif$i-$j.dat 
    #mv concentrations concentrations$i-$j
  done
done
