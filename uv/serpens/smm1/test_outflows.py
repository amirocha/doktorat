from Ncalculation_v3 import calculate_mass 

def test_calculate_mass():
	flux = 3
	mol = 'cn10'
	D = 300*pow(10,18)
	M_outflow = 0
	T_ex=75

	mass = calculate_mass(flux, mol, D, M_outflow, T_ex)

	assert mass == 0.01


