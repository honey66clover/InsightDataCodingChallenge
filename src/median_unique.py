import sys
import numpy as np
from sets import Set

inputfile = sys.argv[1]
outputfile = sys.argv[2]
#punctuations = list(string.punctuation)+["'s"]
histogram = np.zeros(145, dtype=np.uint64) #this numpy array is to store the counts of each integer
#Twitter limits Tweet length to 140 characters, so the integers are in the range [0,140]
#the data type uint64 means it can count 2^64 = 18446744073709551615 tweets at least
#assuming 700 million tweets per day then 20 billion per month.
total_count = 0 #total numbers of integers, int are automatically promoted to long, no overflow problem

	

#given current histogram and current total counts, return the median
def find_median(histo, count): 
	sum = 0
	for i in range(0,len(histo)):
		sum += histo[i]
		if sum > (count+1)/2:
			return i
		if sum == (count+1)/2:
			if (count%2==0 and i<len(histo)-1):
				for j in range(i+1,len(histo)):
					if histo[j]>0:
						return float(i+j)/2 #in case of even events
			else:
				return i

wfile = open(outputfile, 'w') #file to write into
rfile = open(inputfile,'r')
for line in rfile.xreadlines(): #read each line, xreadlines for big files 
	unique_words = Set(line.split())
	wordcount = len(unique_words)
	total_count += 1
	histogram[wordcount]+=1
	wfile.write(str(find_median(histogram, total_count))+'\n')
rfile.close()
wfile.close()

