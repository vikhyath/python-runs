# Given a string A and B, find the smallest substring of A that 
# contains all the characters from B. (implement solution in O(n),
#  keep in mind chars in B can repeat)

#!/usr/bin/env python

A = 'abcxorasddcaoirebancdc'
B = 'abcc'

values = {}
for char in B:
	if char not in values:
		values[char] = 0

	values[char] += 1

start = 0
end = 0
bestsofar = 0
startsofar = 0
endsofar = 0
while end < len(A):
	matches = 0
	temp = values.copy()
	for i in A[start: end+1]:
		if i in temp and temp[i] > 0:
			temp[i] -= 1
			matches += 1

	if matches < len(B):
		end += 1
		continue

	# enough matches, locate start and end
	if not bestsofar or end+1 - start < bestsofar:
		bestsofar = end+1 - start
		startsofar = start
		endsofar = end

	start += 1

print(A[startsofar:endsofar+1])
print(bestsofar)



