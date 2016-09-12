#!/usr/bin/env python
arr = [1, 4, 5, 9, 10, 22, 30, 40]
def binsearch(arr, left, right, target):
	if left > right:
		return False
	mid = int((left + right)/2)
	if arr[mid] == target:
		return True
	if arr[mid] < target:
		return binsearch(arr, mid+1, right, target)
	else:
		return binsearch(arr, left, mid-1, target)

print(binsearch(arr, 0, len(arr)-1, 22))