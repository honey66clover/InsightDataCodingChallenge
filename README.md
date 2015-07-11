# InsightDataCodingChallenge
The programs are executed simply by run.sh

Time complxity analysis:
Problem 1:
Twitter limits tweet length to 140 characters so the time complexity of wordcount is O(n) where n is the numbers of the tweets.
However, sorting the words takes O(nlogn) where n is the numbers of the unique words.
Problem2:
We use an analogy of counting sort, a histogram to store the countings of the integers. The construction of the histogram is O(n) where n is the numbers of the tweets. We keep track of the histogram and the total counts when a tweet comes in. We find the current median according to the histogram by summing the counts when it reaches half of the total counting. The histogram array has length same as the limit of the tweets length, 140, and so finding a median takes O(1) whenever an integer comes in. Altogether the program takes O(n) time.
