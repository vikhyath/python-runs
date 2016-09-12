# Given a collection of candidate numbers (C) and a target number (T),
#  find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 

# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

#!/usr/bin/env python

def summer(arr, target):
	start = 0
	arr = sorted(arr)
	def sow(arr, start, target):
		if target == 0:
			return [[]]

		ret = []
		for idx in range(start, len(arr)):
			if arr[idx] > target:
				break

			if idx != start and arr[idx] == arr[idx-1]:
				continue

			for curr in sow(arr, idx+1, target-arr[idx]):
				ret.append([arr[idx]] + curr)

		return ret

	return sow(arr, start, target)

# print(summer([10, 1, 2, 7, 6, 1, 5], 8))
print(summer([1, 1, 3, 5], 4))