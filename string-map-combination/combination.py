# You are given a string "abc" which is encoded like "123" where alphabets are mapped like a => 1 to z => 26. Now find out how many string can be formed by reverse engineering encode string "123". 

# For ex. given string "123" we can form 3 string "abc"(1,2,3), "lc" (i.e 12,3), "aw"(1,23). 

# for string "1234" we have following possible combinations, I might be missing some of them but you get the idea 

# {12, 3, 4} 
# {1, 23, 4} 
# {1, 2, 3, 4}

# astr = "123"

# 12 -> 1,2
# 123 -> 1,23 | 1,2,3 | 12,3

# 1234 -> 123,4 | 12,34 | 1,234 | 1,2,3,4 | 1,23,4 | 12,3,4 | 1,2,34

# 123 -> 1 + sol(23) -> 2 + sol(3) -> sol('')
#            -> 23 + sol('')
#     -> 12 + sol(3) -> sol('')

lists = []
def somefunc(astr):
	local = []
	print('in: ' + astr)
	if len(astr) == 1:
		print('returning: ' + astr)
		return astr

	x = 0
	while x < len(astr) - 1:
		print('for: ' + astr)
		if x+1 < len(astr):
			ret = somefunc(astr[x+1:])
			print('ret for: ' + astr[x+1:] + ' x+1 is ' + str(x+1) + ' and len(astr) is: ' + str(len(astr)))
			print(ret)
		x += 1

	print('----------------------- end of: ' + astr)

somefunc("123")
print(lists)