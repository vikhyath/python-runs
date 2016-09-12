# Given an array of positive, unique, increasingly sorted numbers A,
#  e.g. A = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13]. 
#  Given a positive value K, e.g. K = 3. 
#  Output all pairs in A that differ exactly by K. 
# e.g. 
# 2, 5 
# 3, 6 
# 5, 8 
# 6, 9 
# 8, 11 
# 9, 12 
# what is the runtime for your code?

import sys
arr = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13]
arr = [1, 2, 3, 5, 6, 8, 12, 15, 16, 17, 18, 20]

start = 0
end = 1

while start < end:
	if arr[end] - arr[start] == 3:
 		print(str(arr[start]) + ' , ' + str(arr[end]))
 		start += 1
 		if end + 1 < len(arr):
 			end += 1
	
	elif arr[end] - arr[start] > 3 or end == len(arr) - 1:
 		start += 1

	if end + 1 < len(arr) and arr[end] - arr[start] < 3:
 		end += 1
