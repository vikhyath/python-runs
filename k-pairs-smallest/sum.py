# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

# You are given two integer arrays nums1 and nums2 sorted in
#  ascending order and an integer k.

# Define a pair (u,v) which consists of one element from 
# the first array and one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Example 1:
# Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

# Return: [1,2],[1,4],[1,6]

# The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

#!/usr/bin/env python

import heapq

def push(heap, num1, num2, i, j):
	if i < len(num1) and j < len(num2):
		heapq.heappush(heap, [num1[i] + num2[j], i, j])

def pairme(num1, num2, i, j, target):
	pairs = []
	heap = []
	push(heap, num1, num2, i, j)

	while len(pairs) < target and heap:
		summer, i, j = heapq.heappop(heap)
		pairs.append((num1[i], num2[j]))

		push(heap, num1, num2, i, j+1)

		if j == 0:
			i += 1
			push(heap, num1, num2, i, j)

	return pairs

print(pairme([1,7,11], [2,4,6], 0, 0, 9))