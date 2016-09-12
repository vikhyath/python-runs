# x = [5, 3, 2, 1, 4]
# y = [5, 3, 2, 1]

# k = 5, 4
# k = k/2 = 2, 2
# node = k - 1 = 3, 3
# 2*node + 1 = 1, 1
# 2*node + 2 = 4, NaN

import math

def swap(arr, idx1, idx2):
	temp = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = temp

def heapify(arr, node, length):
	mini = None
	left = 2 * node + 1
	right = 2 * node + 2
	if node >= 0:
		mini = node

		if left <= length and arr[left] < arr[mini]:
			mini = left

		if right <= length and arr[right] < arr[mini]:
			mini = right

		if mini != node:
			swap(arr, mini, node)
			heapify(arr, mini, length)

def runheap(arr):
	remaining = len(arr) - 1
	while (remaining > 0):
		swap(arr, 0, remaining)
		remaining -= 1
		heapify(arr, 0, remaining)

def buildheap(arr):
	k = math.floor(len(arr) / 2)
	while (k > 0):
		node = k - 1
		heapify(arr, node, len(arr)-1)
		k -= 1

	runheap(arr)

x = [5, 4, 3, 2, 6]
buildheap(x)
print(x)
