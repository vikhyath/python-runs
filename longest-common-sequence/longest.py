# http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/

# non dynamic solution is 2^n (we need to generate all leaf nodes)

# somefunc(strA, strB, m, n):
	# if m == 0 or n == 0:
	# 	return 0

	# if strA[m-1] == strB[n-1]:
	# 	return 1 + somefunc(strA, strB, m-1, n-1)
	# else:
	# 	return max(somefunc(strA, strB, m, n-1), somefunc(strA, strB, m-1, n))

# now dynamic solution, good video to see is https://www.youtube.com/watch?v=NnD96abizww

# idea is to tabulate results that can be used later for diff length combinations of both strings

def dynamicSubSequence(strA, strB, m, n):
	matrix = [[None for col in range(0, n+1)] for row in range(0, m+1)]

	for row in range(0, m+1):
		for col in range(0, n+1):
			if row == 0 or col == 0:
				matrix[row][col] = 0
			elif strA[row-1] == strB[col-1]:
				matrix[row][col] = 1 + matrix[row-1][col-1]
			else:
				matrix[row][col] = max(matrix[row][col-1], matrix[row-1][col])

	return matrix[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print(dynamicSubSequence(X, Y, len(X), len(Y)))

