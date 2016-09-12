# Select Kth largest value in the array. Given an unsorted array of size n,
# and a value k. Select the kth largest value from the array. 

# For example: 

# Array is [5, 3, 9, 1], n is 4 
# k = 0 => 9 
# k = 1 => 5 
# k = 3 => 1


#!/usr/bin/env python

import heapq

arr = [5, 3, 9, 1]
k = 2

# maintain max heap (this is a little ugly since heapq does not do max heap
# using heappop and heappush, it does a min heap)
heap = []
for num in arr:
	heapq._heapify_max(heap)
	if len(heap) < k:
		heapq.heappush(heap, num)

	else:
		top = heap[0]

		# if next num is < top then push
		if top > num:
			heap[0] = num

heapq._heapify_max(heap)
print(heap[0])