#!/usr/bin/env python

# Given two arrays/Lists (choose whatever you want to) with sorted 
# and non intersecting intervals. Merge them to get a new sorted 
# non intersecting array/list. 

# Eg: 
# Given: 
# Arr1 = [3-11, 17-25, 58-73]; 
# Arr2 = [6-18, 40-47]; 

# Wanted: 
# Arr3 = [3-25, 40-47, 58-73];

arr1 = ['3-11', '17-25', '58-73']
arr2 = ['6-18', '40-47']
arr3 = []

i = 0
j = 0

while(i<len(arr1) and j<len(arr2)):
	a = arr1[i].split('-')
	a = int(a[0]) # 3
	b = int(a[1]) # 11

	x = arr2[j].split('-')
	x = int(x[0]) # 6
	y = int(x[1]) # 18

	canMerge = False

	if (x <= b):
		if y<= b:
			start = min(a, x)
			arr3.append(str(start) + '-' + str(b))