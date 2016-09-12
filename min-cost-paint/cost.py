# You are given a range [first, last], initially white. You need to paint it black. 
# For this purpose you have a set of triples 
# [(f, l, cost), ...] - where each triple means that you can paint range [f, l] for `cost` coins (limitations: cost is floating point >= 0, f, l, first, last are integers). 
# Find minimum cost needed to paint the whole range [first, last] or return -1 if it's impossible 
# Example:


# [first, last] = [0, 5] and set of triples is
# [[0, 5, 10], [0, 4, 1], [0, 2,5], [2, 5, 1]]
# Clearly the answer is to take [0, 4, 1] and [2, 5, 1] - the total cost will be 2. 
# Another example:


# [first, last] = [0, 5]
# triples are [[1,4, 10], [2, 5, 6]]
# answer is -1, because it's impossible to color whole range.

def findCost(start, end, costs):
	minsofar = -1
	for idx, cost in enumerate(costs):
		if cost[1] < start or cost[0] > start:
			continue

		currcost = None
		if cost[1] >= end:
			currcost = cost[2]

		else:
			if idx+1 < len(costs):
				currcost = findCost(cost[1], end, costs[:idx] + costs[idx+1:])
				if currcost is not None:
					currcost += cost[2]

		if minsofar == -1 or (currcost and minsofar > currcost):
			minsofar = currcost

	return minsofar

print(findCost(0, 5, [[0, 5, 10], [0, 4, 1], [0, 2,5], [2, 5, 1]]))
print(findCost(5, 10, [[0, 5, 10], [0, 4, 1], [0, 2,5], [2, 5, 1], [1, 11, 4]]))
print(findCost(0, 10, [[1, 5, 1], [0, 6, 2], [2, 8, 3], [5, 10, 1], [0, 11, 8]]))
print(findCost(0, 5, [[0, 5, 10], [0, 3, 1], [3, 4, 2], [3, 4, 1], [4, 5, 1], [0, 2, 5]]))
print(findCost(0, 5, [[1,4, 10], [2, 5, 6]]))
print(findCost(0, 5, [(0, 5, 10), (0, 4, 1), (0, 2, 5), (2, 5, 1)]))
print(findCost(0, 5, [(1, 4, 10), (2, 5, 6)]))                  
print(findCost(2, 6, []))                                                                       
print(findCost(2, 6, [(3, 3, 1), (0, 8, 12), (2, 2, 1), (4, 6, 1)]))