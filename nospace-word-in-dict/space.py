# Given a string where in each word letters were randomly shuffled 
# and after that words were written without spaces (lets call it X). 
# Also you have a dictionary. The task is to return all possible 
# strings S that can be transformed into the string X and all words 
# in S are from dictionary.

#!/usr/bin/env python

X = 'ymacr'

dictionary = ['camry', 'car', 'arc', 'myarc', 'my']

realdict = {}

for word in dictionary:
	sword = ''.join(sorted(word))
	if sword not in realdict:
		realdict[sword] = {}
	if word not in realdict[sword]:
		realdict[sword][word] = 0

	realdict[sword][word] += 1

def checkme(X, dictionary):
	idx = 0
	count = 0
	sortedSoFar = []
	while idx < len(X):
		if X[idx] in dictionary:
			count += 1

		sortedSoFar.append(X[idx])
		sortedSoFarString = ''.join(sorted(sortedSoFar))

		if sortedSoFarString in dictionary:
			local = len(list(dictionary[sortedSoFarString].keys()))

			# multiple this with the recursive substring call
			multiple = 0
			if idx + 1 < len(X):
				multiple = checkme(X[idx+1:], dictionary)			

			count += local if multiple == 0 else multiple * local

		idx += 1

	return count

print(checkme(X, realdict))