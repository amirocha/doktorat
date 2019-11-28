'''CN/HCN statistics'''
import statistics


SMM = [0.61, 0.65, 0.85, 0.47, 0.67, 0.81, 0.43, 0.24, 0.41, 0.71]

outflow = [0.58, 0.51, 0.13, 0.25, 0.56]

class0 = [0.61, 0.65, 0.85, 0.43, 0.24]
class1 = [0.47, 0.67, 0.81, 0.41, 0.71]

#early = [0.65, 0.38, 0.94, 0.67, 0.81] #early class0 only
#late = [0.60, 0.89, 0.37, 0.68, 0.56] #late class0 and class 1

lists = [SMM, outflow, class0, class1]
lists_names = ['SMM', 'outflow', 'class0', 'class1']

def means(data):
	return statistics.mean(data)

def medians(data):
	return statistics.median(data)

def standard_deviations(data):
	return statistics.stdev(data)

def main():  

	integrals=[]
	file2=open('statistics.txt','w')
	file2.write('Sample     Mean     Median    Standard deviation\n')
	for i in range(len(lists)):
		mean = means(lists[i])
		median = medians(lists[i])
		stdev = standard_deviations(lists[i])
		file2.write("%s   %f  %f  %f\n" % (lists_names[i], mean, median, stdev))
	file2.close()

	

if __name__ == '__main__': 
	main()

