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


def do_very_difficult_and_important_for_humanity_operations_on_star_data(data, lenghts):
    base_colors = 'k.;k.;k.;r.;r.;r.;r.;b.;b.;g.;g.;k*;k*;b*'.split(';')
    some_numbers = data.split()
    star_name = some_numbers.pop(0)
    points = []
    colors = []
    for i in range(len(some_numbers)):
        if float(some_numbers[i]) > 0.:
            points.append((lenghts[i], m.log(float(some_numbers[i])/(divisors[i]*1000.)))) 
            colors.append(base_colors[i])

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


def main():
    data = read_data('sed.txt')
    wave_lenghts = [float(lenght) for lenght in data[0].split()[1:]]
    herschel_waweleghts=[70,160,]
    for single_star_data in data[1:]:
        title, points, colors = do_very_difficult_and_important_for_humanity_operations_on_star_data(single_star_data, wave_lenghts)
        make_very_nice_picture(title, points, colors)


if __name__ == '__main__':
    main()
