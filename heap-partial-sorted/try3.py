#!/usr/bin/env python

arr = [5, 4, 2, 6, 3, 16]

def swap(arr, idx1, idx2):
	temp = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = temp

def heapify(arr, length, index):
	minim = index
	left = 2*index + 1
	if left <= length and arr[left] < arr[minim]:
		minim = left

	right = 2*index + 2
	if right <= length and arr[right] < arr[minim]:
		minim = right

	if minim != index:
		swap(arr, minim, index)
		heapify(arr, length, minim)

idx = len(arr)/2 - 1
while idx >= 0:
	heapify(arr, len(arr) - 1, idx)
	idx -= 1

idx = len(arr) - 1
while(idx > 0):
	swap(arr, 0, idx)
	idx -= 1
	heapify(arr, idx, 0)

print(arr)
