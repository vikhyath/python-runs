# Given a sorted array and a target value, return the
#  index if the target is found. If not, return the index
#   where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 = 2
# [1,3,5,6], 2 = 1
# [1,3,5,6], 7 = 4
# [1,3,5,6], 0 = 0

#!/usr/bin/env python

def search(arr, high, low, target):
	if low >= high:
		if target > arr[low]:
			return low + 1
		else:
			return low

	mid = int((low + high) / 2)

	if arr[mid] == target:
		return mid

	if arr[mid] > target:
		high = mid - 1

	else:
		low = mid + 1

	return search(arr, high, low, target)

def searchv2(arr, target):
	low = 0
	high = len(arr) - 1

	while low < high:
		mid = int ((low + high) / 2)

		if arr[mid] >= target:
			high = mid

		else:
			low = mid + 1

	if arr[low] < target:
		return low + 1
	else:
		return low

print(search([1, 3, 5, 7], 3, 0, 8))

print(searchv2([1, 3, 5, 7], 6))