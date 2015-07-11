import sys, collections

inputfile=sys.argv[1]
outputfile=sys.argv[2]
wordcount = {} #dictionary to store the words and the counts
wfile = open(outputfile, 'w') #output file
rfile = open(inputfile,'r') #input file
for line in rfile.xreadlines(): #read each tweet, use xreadlines for big files 
	for word in line.split(): #read each word, split by white space
		if word in wordcount:
			wordcount[word] += 1
		else:
			wordcount[word] = 1
rfile.close()
ordered_wordcount = collections.OrderedDict(sorted(wordcount.items()))
for k,v in ordered_wordcount.items():
	wfile.write(k+"\t"+str(v)+"\n")
wfile.close()