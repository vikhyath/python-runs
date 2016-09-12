# input a list of array [[1, 2, 3], [1], [1, 2]] 
# return the list of array, each array is a combination of one 
# element in each array.
# [[1, 1, 1], [1, 1, 2], [2, 1, 1], [2, 1, 2], [3, 1, 1], [3, 1, 2]]

#!/usr/bin/env python

def exists(array, val, start, end):
	if start == end:
		return array[start] == val

	mid = int((start + end)/2)

	if array[mid] == val:
		return True

	return exists(array, val, start, mid-1) or exists(array, val, mid+1, end)

arr = [[1, 2, 3], [1], [1, 2]]
target = 4
res = []
for val2 in arr[2]:
	for val1 in arr[1]:

		# do a binary search and find if val0 exists in arr0

		if exists(arr[0], target-val1-val2, 0, len(arr[0]) - 1):
			res.append([val2, val1, target-val1-val2])

print(res)