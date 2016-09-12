

def heapify(arr, length, idx):
	mini = idx
	if (2*idx + 1) < length and arr[2*idx+1] < arr[mini]:
		mini = 2*idx+1

	if 2*idx + 2 < length and arr[2*idx+2] < arr[mini]:
		mini = 2*idx+2

	if mini != idx:
		temp = arr[mini]
		arr[mini] = arr[idx]
		arr[idx] = temp

		heapify(arr, length, mini)

arr = [5, 4, 3, 1, 6]

idx = int((len(arr) / 2)) - 1

while (idx >= 0):
	heapify(arr, len(arr), idx)
	idx -= 1

idx = len(arr)
while(idx > 1):
	temp = arr[0]
	arr[0] = arr[idx - 1]
	arr[idx - 1] = temp	
	idx -= 1
	heapify(arr, idx, 0)

print(arr)