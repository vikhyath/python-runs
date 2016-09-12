
x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_here = max_so_far = x[0]
startidx = -1
endidx = -1

for idx, num in enumerate(x[1:]):
	max_here = max(num,  max_here + num)
	if max_here == num:
		startidx = idx + 1

	max_so_far = max(max_so_far, max_here)
	if max_so_far == max_here:
		endidx = idx + 1

print(max_so_far)
print(x[startidx: endidx+1])
