# Given a random string S and another string T with unique elements, 
# find the minimum consecutive sub-string of S such that 
# it contains all the elements in T. 

# example: 
# S='adobecodebanc' 
# T='abc' 
# answer='banc'

counts = {}
currWindow = {}

S='adobecodebanc' 
T='abc'

dist = 0
idx = 0 # end
start = 0
bestStart = 0
bestEnd = 0

while idx < len(T):
	if S[idx] not in currWindow:
		currWindow[S[idx]] = 0
	currWindow[S[idx]] += 1

	idx += 1

while start < len(S):
	# check if all chars exist in currWindow which are in T
	matches = 0
	for x in T:
		if x in currWindow and currWindow[x] > 0:
			matches += 1

	if matches < len(T) and idx < len(S):
		if S[idx] not in currWindow:
			currWindow[S[idx]] = 0
		currWindow[S[idx]] += 1
		idx += 1
		continue

	elif matches >= len(T):
		if not dist or dist > idx - start:
			dist = idx - start
			bestEnd = idx
			if idx == len(S):
				bestEnd -= 1
			bestStart = start
	currWindow[S[start]] -= 1
	start += 1

print(S[bestStart:bestEnd+1])
