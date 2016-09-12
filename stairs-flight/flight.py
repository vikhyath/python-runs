# https://leetcode.com/problems/climbing-stairs/
# ends up being a fibonacci series 

def climb(n):
	step1 = 0
	step2 = 1
	currstep = 1
	i = 0
	while(i < n):
		currstep = step1 + step2
		step1 = step2
		step2 = currstep
		i += 1

	return currstep

print(climb(0)) # -> 1
print(climb(1)) # -> 1
print(climb(2)) # -> 2
print(climb(3)) # -> 1,1,1 | 1,2 | 2,1 : 3
print(climb(4)) # -> 1,1,1,1 | 1,2,1 | 1,1,2 | 2,2 | 2, 1, 1
print(climb(5)) # -> 7