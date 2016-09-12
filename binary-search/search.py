arr = [1, 4, 16, 3, -9, 8, 7, 0]
arr = sorted(arr)

def binsearch(arr, find, start, end):
	if start > end:
		return (False, False)
	mid = start + int((end - start) / 2)
	if arr[mid] == find:
		return (True, mid)
	if arr[mid] < find:
		return binsearch(arr, find, mid+1, end)
	else:
		return binsearch(arr, find, start, mid-1) 

print(arr)
print(binsearch(arr, 4, 0, len(arr)-1))