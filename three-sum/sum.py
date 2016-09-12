# Given an array S of n integers, are there elements a, b, c in S 
# such that a + b + c = 0? Find all unique triplets in the array 
# which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# https://leetcode.com/problems/3sum/

#!/usr/bin/env python

def threesum(arr):
	arr = sorted(arr)

	if len(arr) < 3:
		return None

	res = []

	for idx in range(len(arr) - 2):
		if idx == 0 or (idx > 0 and arr[idx] != arr[idx-1]):
			jack = idx + 1
			tail = len(arr) - 1

			while jack < tail:
				summer = arr[idx] + arr[jack] + arr[tail]
				if summer == 0:
					res.append([arr[idx], arr[jack], arr[tail]])
					while (jack < tail and arr[jack] == arr[jack+1]):
						jack += 1
					while (jack < tail and arr[tail] == arr[tail-1]):
						tail -= 1

					jack += 1
					tail -= 1

				elif summer > 0:
					tail -= 1

				elif summer < 0:
					jack += 1

	return res

print(threesum([-1, -1, 0, 1, 2, 4]))
print(threesum([0,0,0,0]))