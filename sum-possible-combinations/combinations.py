# Given a number N, write a program that returns all possible combinations of numbers that add up to N, as lists. (Exclude the N+0=N) 

# For example, if N=4 return {{1,1,1,1},{1,1,2},{2,2},{1,3}}

def comb(n, start, nums, arr=[]):
	if len(arr) == 0:
		arr = [None for y in range(0, nums+1)]

	if (n == 0):
		for i in range(0, start):
			print(arr[i], end=',')
		print('')

	elif(n > 0):
		for i in range(1, nums+1):
			arr[start] = i
			comb(n-i, start+1, i, arr)

comb(4, 0, 3, [])
