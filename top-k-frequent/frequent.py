# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 <= k <= number of unique elements.
# Your algorithms time complexity must be better than O(n log n),
# where n is the array's size.

#!/usr/bin/env python

import heapq

arr = [1, 2, 4, 1, 3, 1 , 2, 4, 4, 4, 9, 3, 8]
freq = 2

vals = {}
for ele in arr:
	if ele not in vals:
		vals[ele] = 0

	vals[ele] += 1

heap = []
for ele, count in vals.items():
	heapq.heappush(heap, [count, ele])

while len(heap) > freq:
	heapq.heappop(heap)

print(heap)