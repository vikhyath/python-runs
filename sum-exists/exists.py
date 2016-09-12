# Given an array of positive integers and a target total of X, find if there exists a contiguous subarray with sum = X 

# [1, 3, 5, 18] X = 8 Output: True 
# X = 9 Output: True 
# X = 10 Output: False 
# X = 40 Output :False

# O(N^2)
def test(alist, target):
	sofar = 0
	idx = 0
	start = idx
	while True:
		if idx == len(alist):
			break

		sofar += alist[idx]
		if target == sofar:
			print(str(start) + ' -> ' + str(idx))
			return

		if sofar > target:
			idx = start + 1
			start = idx
			sofar = 0

			continue

		idx += 1

	print('NO')

# O(N)
def newtest(alist, target):
	start = 0
	end = 0
	sofar = 0
	while True:
		if end == len(alist) or start == len(alist):
			break

		if start > end:
			end = start
			continue

		sofar = sum(alist[start:end+1])

		if sofar == target:
			print(str(start) + ' -> ' + str(end))
			return

		if target > sofar:
			end += 1

		if target < sofar:
			start += 1

	print('NO')

test([1,3,5,18], 18)
test([1,3,5,18], 8)
test([1,3,5,2,18], 10)

newtest([1,3,5,18], 18)
newtest([1,3,5,18], 8)
newtest([1,3,5,2,18], 10)
newtest([1,3,5,2,18], 0)
newtest([1,3,5,2,18], 100)