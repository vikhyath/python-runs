# There are N coins with coordinates (x, y) where x >0 and y >0 
# You start at (0, 0) and you can only do steps of form (dx, dy) where dx >0 and dy > 0 
# Print the maximum number of coins that you can collect. 

# Clarification: you can do as many moves as you wish, the point is to collect maximum number of coins. If you are located at position (a, b) you may jump to position (a+dx, b+dy) for all dx > 0 and dy > 0 

# Assumptions: Input is a 2D Matrix of integers where 1 represents a coin being present and 0 represents no coin
# Approach: Dynamic programming with recursion and caching.

ip = [[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

sol = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]

def getMax(ip, sol, row, col):
	if (sol[row][col] != -1):
		return sol[row][col]

	maxcoins = 0

	for i in range(1,len(ip)):
		for j in range(1, len(ip[0])):
			if row+i < len(ip) and col+j < len(ip[0]):
				maxcoins = max(maxcoins, getMax(ip, sol, row+i, col+j))

	maxcoins += ip[row][col]
	sol[row][col] = maxcoins
	return maxcoins

print(getMax(ip, sol, 0, 0))
print(sol)