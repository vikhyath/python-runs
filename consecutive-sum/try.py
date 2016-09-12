# Given an array of positive integers and a target total of X, 
# find if there exists a contiguous subarray with sum = X 

# [1, 3, 5, 18] X = 8 Output: True 
# X = 9 Output: True 
# X = 10 Output: False 
# X = 40 Output :False

#!/usr/bin/env python

arr = [23, 5, 4, 7, 2, 11]
target = 18

start = 0
end = start

summer = arr[end]
while end < len(arr) and start < len(arr):
	summer = sum(arr[start:end+1])
	if summer == target:
		print(arr[start:end+1])
		break

	if summer < target:
		end += 1

	if summer > target:
		summer -= arr[start]
		start += 1