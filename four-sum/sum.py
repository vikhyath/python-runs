# Given an array S of n integers, are there elements a, b, c, 
# and d in S such that a + b + c + d = target? Find all unique 
# quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

#!/usr/bin/env python

def four(arr, target):
	if not arr or len(arr) < 4:
		return []

	arr = sorted(arr)
	res = []
	for i in range(len(arr)-3):
		if i == 0 or (i > 0 and arr[i] != arr[i-1]):
			for j in range(i+1, len(arr)-2):
				if j == i + 1 or (j > i + 1 and arr[j] != arr[j-1]):
					jack = j + 1
					tail = len(arr) - 1

					while (jack < tail):
						summer = arr[i] + arr[j] + arr[jack] + arr[tail]
						if summer == target:
							res.append([arr[i], arr[j], arr[jack], arr[tail]])

							while (jack < tail and arr[jack] == arr[jack+1]):
								jack += 1

							while (jack < tail and arr[tail] == arr[tail-1]):
								tail -= 1

							jack += 1
							tail -= 1

						elif summer < target:
							jack += 1

						else:
							tail -= 1

	return res

print(four([1, 0, -1, 0, -2, 2], 0))
print(four([0,0,0,0], 0))

