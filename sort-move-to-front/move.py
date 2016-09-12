# You have an array of unique integer numbers and only 
# one operation: MoveToFront(x) that moves given number to the beginning of the array. 
# Write a program to sort the array using the minimum possible number of MoveToFront() calls.

# heap -> max heap, move to front 

alist = [4,1,5,0,6,2]

def moveToFront(idx, pos):
	copy = alist[idx]
	start = idx
	while(start > pos):
		alist[start] = alist[start-1]
		start -= 1

	alist[pos] = copy

i = 0
while (i < len(alist)):
	j = i
	minimum = j
	while (j < len(alist)):
		if alist[j] < alist[minimum]:
			minimum = j
		j +=1
	moveToFront(minimum, i)
	i +=1 

print(alist)