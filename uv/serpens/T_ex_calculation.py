'''T_ex calculation for H13CN 1-0 and H13CN 2-1 from Itrich (bachelor thesis, p.35)'''
import math as m

c = 299792458 #[m/s]

E2 = 12.43
E1 = 4.14

nu1 = 86.340184
nu2 = 172.677881
lamda1 = c/nu1
lamda2 = c/nu2

I1_SMM4 = 1.613614
I2_SMM4 = 0.813298
I1_SMM9 = 2.36894
I2_SMM9 = 1.814535

A1 = 1.512E-5
A2 = 6.90E-5

g1 = 3
g2 = 5


def equation(E1, E2, lamda1, lamda2, I1, I2, A1, A2, g1, g2):
	T_ex = (E2-E1) * m.pow(m.log((lamda1*I1*A2*g2)/(lamda2*I2*A1*g1)),-1)
	return T_ex


print('SMM4', equation(E1, E2, lamda1, lamda2, I1_SMM4, I2_SMM4, A1, A2, g1, g2))
print('SMM9', equation(E1, E2, lamda1, lamda2, I1_SMM9, I2_SMM9, A1, A2, g1, g2))
