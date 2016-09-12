# There are N coins with coordinates (x, y) where x >0 and y >0 
# You start at (0, 0) and you can only do steps of form (dx, dy) 
# where dx >0 and dy > 0. Print the maximum number of coins that
#  you can collect. 

# Clarification: you can do as many moves as you wish, the point 
# is to collect maximum number of coins. If you are located at 
# position (a, b) you may jump to position (a+dx, b+dy) for 
# all dx > 0 and dy > 0 

#!/usr/bin/env python

coins = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0]]
sums = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]

# sums = [[-1] * len(coins[0])] * len(coins)

print(type(sums))

def maxcoins(coins, sums, row, col):
	if row == len(coins) and col == len(coins[0]):
		return 0

	if sums[row][col] != -1:
		return sums[row][col]

	# now iterate over x and y and then pick best max
	maxpicked = 0
	for i in range(row+1, len(coins)):
		for j in range(col+1, len(coins[0])):
			if i < len(coins) and j < len(coins[0]):
				picked = maxcoins(coins, sums, i, j)
				if picked > maxpicked:
					maxpicked = picked


	maxpicked += coins[row][col]
	sums[row][col] = maxpicked

	return maxpicked

print(maxcoins(coins, sums, 0, 0))
print(sums)