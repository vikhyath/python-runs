#!/usr/bin/env python

# Given two arrays/Lists (choose whatever you want to) 
# with sorted and non intersecting intervals. Merge them 
# to get a new sorted non intersecting array/list. 

# Eg: 
# Given: 
# Arr1 = [3-11, 17-25, 58-73]; 
# Arr2 = [6-18, 40-47]; 

# Wanted: 
# Arr3 = [3-25, 40-47, 58-73];

arr1 = ['3-11', '17-25', '58-73']
arr2 = ['6-18', '40-47', '67-90']

def splitme(string):
	string = string.split('-')
	return (int(string[0]), int(string[1]))

def what(arr1, i, arr3, j):
	a, b = splitme(arr1[i])
	x, y = splitme(arr3[j])

	popped = arr3.pop()
	if a <= y or a + 1 == y: # 3-7, 4-6 | 7-11 | 6-11
		if b <= y: # 3-7, 4-6
			arr3.append(popped)

		else: # 3-7, 7-11 | 6-11
			arr3.append(str(x) + '-' + str(b))
	else: # 3-7, 9-12
		arr3.append(popped)
		arr3.append(arr1[i])

i = 0
j = 0
arr3 = []
while (i < len(arr1) or j < len(arr2)):
	if i < len(arr1):
		a, b = splitme(arr1[i])
	else:
		a = None

	if j < len(arr2):
		x, y = splitme(arr2[j])
	else:
		x = None

	if a is not None and (x is None or a <= x):
		if not len(arr3):
			arr3.append(arr1[i])

		what(arr1, i, arr3, len(arr3) - 1)
		i += 1
	else:
		if not len(arr3):
			arr3.append(arr2[j])

		what(arr2, j, arr3, len(arr3) - 1)
		j += 1

print(arr3)