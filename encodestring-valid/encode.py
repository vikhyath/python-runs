# You are given a string "abc" which is encoded like "123" 
# where alphabets are mapped like a => 1 to z => 26. 
# Now find out how many string can be formed by reverse 
# engineering encode string "123". 

# For ex. given string "123" we can form 
# 3 string "abc"(1,2,3), "lc" (i.e 12,3), "aw"(1,23). 

# for string "1234" we have following possible combinations, 
# I might be missing some of them but you get the idea 

# {12, 3, 4} 
# {1, 23, 4} 
# {1, 2, 3, 4}

#!/usr/bin/env python

astring = "11111"

def isvalid(num):
	return int(num) >= 1 and int(num) <= 26

def checkme(astring):
	if len(astring) == 0 or len(astring) == 1:
		return 1

	num = 0
	num += checkme(astring[1:])
	if isvalid(astring[0:2]):
		if len(astring) >= 3:
			num += checkme(astring[2:])
		elif len(astring) == 2:
			num += 1


	return num

print(checkme(astring))