# Given an unsorted array return whether an increasing subsequence of 
# length 3 exists or not in the array.

# Formally the function should:
# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else 
# return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Examples:
# Given [1, 2, 3, 4, 5],
# return true.

# Given [5, 4, 3, 2, 1],
# return false.

#!/usr/bin/env python

arr = [3, 10, 6, 4, 5]
c1 = -1
c2 = -1
c3 = -1

for ele in arr:
	if c1 == -1 or ele <= c1:
		c1 = ele

	elif c2 == -1 or ele <= c2:
		c2 = ele

	else:
		print(c1)
		print(c2)
		print(ele)
		break