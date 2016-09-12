def num(n):
	a = 0
	ctr = 0 
	if a <= n:
		print(a)
		ctr += 1
	b = 1
	if b <= n:
		print(b)
		ctr += 1
	c = a + b
	while (c <= n):
		ctr += 1
		print(c)
		a = b
		b = c
		c = a + b

	print(ctr)

num(1000)
