# A museum was represented by a square matrix that was filled with O, G, 
# and W where O represented open space G represented guards, and W 
# represented walls. Write a function that accepts the square matrix and 
# returns another square matrix where all of the Os in the matrix are 
# replaced with the number of how many spaces they are away from a guard, 
# without being able to go through any walls.

#!/usr/bin/env python

from collections import deque

matrix = [['o', 'o', 'o', 'g', 'o'], ['g', 'o', 'w', 'o', 'o'], ['o', 'g', 'o', 'o', 'w'], ['o', 'w', 'g', 'o', 'o'], ['w', 'o', 'o', 'o', 'g']]

class Position:
	def __init__(self, i, j, dist):
		self.i = i
		self.j = j
		self.dist = dist

res = []
queue = deque()

for i in range(len(matrix)):
	res.append([])
	for j in range(len(matrix[0])):
		res[i].append(-1)
		if matrix[i][j] == 'g':
			queue.append(Position(i, j, 0))
			res[i][j] = 0

def isValid(matrix, i, j):
	if i == len(matrix) or j == len(matrix[0]) or i < 0 or j < 0 or res[i][j] != -1 or matrix[i][j] == 'w':
		return False
	return True

def updateNeighbors(pos, matrix, res, queue):
	neighbors = [[0, 1], [0, -1], [1, 0], [0, 1]]
	for neigh in neighbors:
		# if valid neighbor, then update dist and add to queue
		if isValid(matrix, pos.i + neigh[0], pos.j + neigh[1]):
			res[pos.i + neigh[0]][pos.j + neigh[1]] = pos.dist + 1
			queue.append(Position(pos.i + neigh[0], pos.j + neigh[1], pos.dist + 1))

while len(queue):
	pos = queue.popleft()

	updateNeighbors(pos, matrix, res, queue)

print(res)