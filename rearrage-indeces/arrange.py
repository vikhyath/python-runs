# We have an array of objects A and an array of indexes B.
# Reorder objects in array A with given indexes in array B. 
# Do not change array A's length. 

# example:


# var A = [C, D, E, F, G];
# var B = [3, 0, 4, 1, 2];

# sort(A, B);
# // A is now [D, F, G, C, E];

A = ['C', 'D', 'E', 'F', 'G']
B = [4,3,1,0,2]

idx = 0
while idx < len(A):
	if B[idx] != idx:
		unsettleA = A[idx]
		unsettleB = B[idx]
		while True:
			# settle now!
			tempA = A[unsettleB]
			tempB = B[unsettleB]

			A[unsettleB] = unsettleA
			B[unsettleB] = unsettleB

			if B[tempB] != tempB:
				unsettleA = tempA
				unsettleB = tempB
			else:
				break

	idx += 1

print(A)
print(B)