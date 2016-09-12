# Suppose a sorted array is rotated at some pivot unknown 
# to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array
#  return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# https://leetcode.com/problems/search-in-rotated-sorted-array/

def searchrotated(alist, target, low=None, high=None):
	if low is None:
		low = 0
		high = len(alist) -1 

	if low > high:
		return -1

	if low == high:
		if alist[low] == target:
			return low
		else:
			return -1

	middle = int((low + high) / 2)

	if alist[middle] == target:
		return middle
	else:
		if alist[middle] <= alist[high]:
			if alist[middle] < target and target <= alist[high]:
				return searchrotated(alist, target, middle+1, high)
			else:
				return searchrotated(alist, target, low, middle-1)
		else:
			if alist[low] <= target and target < alist[middle]:
				return searchrotated(alist, target, low, middle-1)
			else:
				return searchrotated(alist, target, middle+1, high)

print(searchrotated([4, 5, 6, 7, 8, 9, 10, 0, 1, 2], 10))
print(searchrotated([4,5,6,7,0,1,2], 4))
print(searchrotated([4,5,6,7,0,1,2], 0))
print(searchrotated([1,3], 4))