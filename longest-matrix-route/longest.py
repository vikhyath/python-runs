#!/usr/bin/env python

# question: https://s31.postimg.org/7nwp4gmzv/hurdle1.jpg

# How do I find the longest possible route in a matrix? 
# There are some hurdles in the path. 

from copy import deepcopy

ip = '3 10, 3, 1 2, 1 5, 1 8, 0 0, 1 7'

ip = ip.split(',')
dim = ip[0].split(' ')
matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(matrix)
somehistory = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

guards = {}
for i in range(1, int(ip[1]) + 1):
	guards[ip[1 + i].strip()] = 'G'

print(guards)

start = list(map(int, ip[2 + int(ip[1])].strip().split(' ')))
end = list(map(int, ip[3 + int(ip[1])].strip().split(' ')))

print(start)
print(end)

for i in range(len(matrix)):
	print(i)
	for j in range(len(matrix[0])):
		matrix[i][j] = 0

def findLongest(matrix, history, guards, start, end):
	if start[0] >= len(matrix) or start[1] >= len(matrix[0]) or str(start[0]) + ' ' + str(start[1]) in guards \
		or start[0] < 0 or start[1] < 0 or history[start[0]][start[1]] == 1:
		return 0

	if start[0] == end[0] and start[1] == end[1]:
		return 1

	history[start[0]][start[1]] = 1

	down = findLongest(matrix, deepcopy(history), guards, [start[0], start[1] - 1], end)
	up = findLongest(matrix, deepcopy(history), guards, [start[0], start[1] + 1], end)
	right = findLongest(matrix, deepcopy(history), guards, [start[0] + 1, start[1]], end)
	left = findLongest(matrix, deepcopy(history), guards, [start[0] - 1, start[1]], end)

	maximum = max(max(left, right), max(up, down))

	if maximum == 0:
		return 0

	return maximum + 1

print(findLongest(matrix, somehistory, guards, start, end) - 1)
