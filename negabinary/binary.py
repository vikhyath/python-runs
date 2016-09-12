# Given a decimal number, write a function that returns its negabinary 
# (i.e. negative 2-base) representation as a string.


# #!/usr/bin/env python3
# assert solution(-15) ==	'110001'
# assert solution(2) == '110'
# assert solution(13) == '11101'


# The algorithm is described in 
# http://en.wikipedia.org/wiki/Negative_base#Calculation. 
# Basically, you just pick the remainder as the positive base case 
# and make sure the remainder is nonnegative and minimal.

#  7 = -3*-2 + 1  (least significant digit)
# -3 =  2*-2 + 1
#  2 = -1*-2 + 0
# -1 =  1*-2 + 1
#  1 =  0*-2 + 1  (most significant digit)

#!/usr/bin/env python

def nega(num):
	res = []
	while num != 0:
		remainder = abs(num) % 2
		res.append(str(remainder))
		if num < 0 and remainder:
			num -= 1
		num = int(num / -2)

	print(''.join(reversed(res)))

nega(-15)
nega(2)
nega(13)
nega(7)