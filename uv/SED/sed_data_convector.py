'''Convert flux density at mJy to Jy/beam'''
import matplotlib.pyplot as plt
import math as m

twoMASS_beam = 2.5
twoMASS_beam_rad = twoMASS_beam*((2*m.pi)/(360*60*60)) #sr
IRAC_beam = 1.8 #arcsec
IRAC_beam_rad = IRAC_beam*((2*m.pi)/(360*60*60)) #sr
MIPS_24_beam = 6. #arcsec
MIPS_24_beam_rad = MIPS_24_beam*((2*m.pi)/(360*60*60)) #sr
MIPS_70_beam = 18. #arcsec
MIPS_70_beam_rad = MIPS_70_beam*((2*m.pi)/(360*60*60)) #sr
WISE_beam = 60. #arcsec
WISE_beam_rad = WISE_beam*((2*m.pi)/(360*60*60)) #sr
SCUBA_450_beam = 7.9 #arcsec
SCUBA_450_beam_rad = SCUBA_450_beam*((2*m.pi)/(360*60*60)) #sr
SCUBA_850_beam = 13. #arcsec
SCUBA_850_beam_rad = SCUBA_850_beam*((2*m.pi)/(360*60*60)) #sr
Bolocam_beam = 33.
Bolocam_beam_rad = Bolocam_beam*((2*m.pi)/(360*60*60)) #sr

divisors = [
    twoMASS_beam_rad,
    twoMASS_beam_rad,
    twoMASS_beam_rad,
    IRAC_beam_rad,
    IRAC_beam_rad,
    IRAC_beam_rad,
    IRAC_beam_rad,
    MIPS_24_beam_rad,
    MIPS_70_beam_rad,
    WISE_beam_rad,
    WISE_beam_rad,
    SCUBA_450_beam_rad,
    SCUBA_850_beam_rad,
    Bolocam_beam_rad
]

def read_data(filename):
    file = open(filename,'r')
    data = file.readlines()
    file.close()

    return data


def do_very_difficult_and_important_for_humanity_operations_on_star_data(data, herschel_data, lenghts):
    base_colors = 'k.;k.;k.;r.;r.;r.;r.;b.;b.;g.;g.;k*;k*;b*'.split(';')
    herschel_colors = '0;m*;m*;m*;m*;m*'.split(';')
    herschel_wawelenghts=[0,70,160,250,350,500]
    some_numbers = data.split()
    print(some_numbers)
    star_name = some_numbers.pop(0)
    points = []
    colors = []
    for i in range(len(some_numbers)):
        if float(some_numbers[i]) > 0.:
            points.append((lenghts[i], m.log10(float(some_numbers[i])/1000.))) #mJy
            colors.append(base_colors[i])
    for i in range(1,len(herschel_data.split())):
        
        if float(herschel_data.split()[i]) > 0.:
            points.append((herschel_wawelenghts[i], m.log10(float(herschel_data.split()[i])))) #Jy
            colors.append(herschel_colors[i])
    
    return star_name, points, colors

 
def make_very_nice_picture(title, points, colors):
    plt.figure(1)
    plt.title(title)
    plt.ylabel("Log(Flux/beam) [Jy]")
    plt.xlabel("Wawelength [microns]")
    
    for i in range(len(points)):
       	plt.plot(points[i][0], points[i][1], colors[i], ms=10)

    #plt.errorbar(CN_HCN,O_OH, yerr=O_OH, linestyle="None")
    plt.savefig(title, format='png')
    plt.close()

def write_to_file(title, points):
    fileend=open('sed_converted','a')
    for i in range(len(points)):
        wavelength=points[i][0]
        flux=10**points[i][1]
        line=str(title)+' '+str(wavelength)+' '+str(flux)+'\n'
        fileend.writelines(line)
    fileend.close()
    

def main():
    data = read_data('sed.txt')
    herschel_data = read_data('herschel_sed.txt')
    wave_lenghts = [float(lenght) for lenght in data[0].split()[1:]]
   
    for i in range(1,len(data)):
        print(i)
        title, points, colors = do_very_difficult_and_important_for_humanity_operations_on_star_data(data[i], herschel_data[i], wave_lenghts)
        #make_very_nice_picture(title, points, colors)
        write_to_file(title, points)


if __name__ == '__main__':
    main()
