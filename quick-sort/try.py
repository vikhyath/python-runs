#!/usr/bin/env python

arr = [ 6, 5, 2, 1, -10]

def sortpivot(arr, start, end):
	pivot = end
	i = start
	j = start - 1
	while i <= end:
		if arr[i] < arr[pivot]:
			j += 1
			# swap
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp

		i += 1

	j += 1
	temp = arr[end]
	arr[end] = arr[j]
	arr[j] = temp

	return j

def quick(arr, start, end):
	if start >= end:
		return

	idx = sortpivot(arr, start, end)
	quick(arr, start, idx-1)
	quick(arr, idx+1 , end)


quick(arr, 0, len(arr) - 1)

print(arr)