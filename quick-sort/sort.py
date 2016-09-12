def swap(arr, a, b):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp

def sort(arr, start, end):
	pivot = arr[end]
	i = start
	j = start

	while (i <= end):
		if arr[i] < arr[end]:
			swap(arr, i, j)
			j += 1

		i += 1

	swap(arr, i-1, j)
	return j

def quick(arr, start, end):
	if start >= end:
		return start

	pos = sort(arr, start, end)
	quick(arr, start, pos-1)
	quick(arr, pos+1, end)


arr = [5, 14, 13, 6, 8, -167]

quick(arr, 0, len(arr)-1)

print(arr)