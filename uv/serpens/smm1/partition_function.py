'''Extrapolate Partition Function'''
import scipy.stats as stat


X = [9.375, 18.75, 37.5, 75, 150, 225, 300]
Q_HCN = [14.272, 27.473, 53.914, 106.807, 212.618, 318.493, 424.326]
Q_CN = [22.7963, 43.4081, 84.7308, 167.4335, 332.9077, 498.4499, 664.0906]
Q_CS = [8.316, 16.285, 32.240, 64.150, 127.968, 191.823, 255.505]
Q_CO = [3.744, 7.122, 13.897, 27.455, 54.581, 81.718, 108.865]


def fit_linear_regression(x, y):
	slope, intercept, r_value, p_value, stderr = stat.linregress(x,y)
	print(slope, intercept, r_value, p_value, stderr)
	return slope, intercept, stderr

def main():
	for func in [Q_HCN, Q_CN, Q_CS, Q_CO]:
		fit_linear_regression(X, func) 



if __name__ == '__main__': 
	main()
