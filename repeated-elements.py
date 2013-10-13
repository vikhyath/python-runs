# Algorithm to find repeated elements, based on the paper "Finding repeated elements" by Misra and Gries.
# Adapted from "A Linear Time Majority Vote Algorithm" http://www.cs.utexas.edu/~moore/best-ideas/mjrty/

# Consider k = 4, n = 9 
# Given array: 3 1 2 2 2 1 4 3 3 
# find all elements in array which repeat more than n/k times

alist = [3, 1, 2, 2, 2, 1, 4, 3, 3]
k = 4

# maintain a dict of size k-1, because at most there can be k-1 distinct elements which have repeatitions > n/k
adict = {} # O(nk)

# loop through the list
# 1. for each element in list, see if you can add to dict  -> O(nk)
# 	1.1 if dict has space, add. if key already exists increment count, if dict is full, decrement 1 from all keys's count in dict
# 	-> O(k)
#	1.2 if some key has a value of 0, remove from dict
# 2. now for each k-1 keys in dict, check if the its repeatition count is actually > n/k -> O(nk)
# 3. linear time algorithm, runs in k*O(n)

# time complexity: O(n)
# space complexity: O(k)

tempdict = {}
for i in alist:
	if i in adict:
		adict[i] += 1
	else:
		if len(adict) < k-1:
			adict[i] = 1
		else:
			for key, val in adict.iteritems():
				adict[key] -= 1
				if adict[key] > 0:
					tempdict[key] = adict[key]
			adict = tempdict
			tempdict = {}

# print adict : now has the most probable set of elements which may be having a count > n/k, note how we reduced our sample
#               size from n to k-1

# now check for each key in dict, if its repeatition count is actually > n/k and print
threshold = len(alist)/k

for key, val in adict.iteritems():
    count = 0
    for e in alist:
        if e == key:
            count += 1
    if count > threshold:
        print key
