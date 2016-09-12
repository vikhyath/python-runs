#!/usr/bin/env python

# Given an array and a number, add it in such a way where array is [0,0,1] 
# and number is 4 output will be [0,0,5] 

# Example 2 : 
# array is [1] and number is 9 output will be [1,0]

from collections import deque

arr = [9,4]
number = 2898 # out = 1 0 2

# 4 + 8 = 12
# carry = 1 (sum/10), num = 2 (sum%10)

# 4+200 = 204
# carry = 20 (sum/10), num = 4 (sum%10)

carry = 0
idx = len(arr)-1
while(True):
	if arr[idx] + number >= 10:
		carry = int((arr[idx] + number) / 10)
		arr[idx] = (arr[idx] + number) % 10
		number = carry
	else:
		arr[idx] += number
		break

	if idx == 0:
		arr = [0] + arr
		idx = 1

	idx -= 1

print(arr)