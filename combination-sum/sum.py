# Given a set of candidate numbers (C) and a target number (T),
#  find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7

#!/usr/bin/env python

def summer(idx, nums, target, res=[], path=[]):
	if target == 0:
		res.append(path)
		return

	if idx >= len(nums) or target < 0:
		return

	summer(idx+1, nums, target, res, path)
	summer(idx, nums, target-nums[idx], res, path+[nums[idx]])

res = []
summer(0, [2,3,6,7], 7, res, [])
print(res)