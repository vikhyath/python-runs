# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

#!/usr/bin/env python

def reverse(integer):
	if not integer:
		print(integer)
		return integer

	x = integer
	sign = -1 if x < 0 else 1
	x = abs(integer)
	num = 0
	while x != 0:
		y = x % 10
		x = int(x / 10)
		num = num * 10 + y

	print(num*sign)

reverse(123)
reverse(0)
reverse(-123)

