x = [5, 4, 2, 10, 1, 0, -9]

i = 1
while (i < len(x)):
	j = i
	while (j > 0):
		if (x[j] < x[j-1]):
			temp = x[j]
			x[j] = x[j-1]
			x[j-1] = temp

		j -= 1

	i += 1

print(x)