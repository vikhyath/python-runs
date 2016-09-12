# Given a string s and a dictionary of words dict, 
# determine if s can be segmented into a space-separated sequence of 
# one or more dictionary words. 

# For example, given 
# s = "leetcode", 
# dict = ["leet", "code"]. 

# Return true because "leetcode" can be segmented as "leet code".

#!/usr/bin/env python

def checkMe(string, words):
	end = 0
	while end < len(string):
		if string[:end+1] in words:
			return True and checkMe(string[end+1:], words) if end + 1 < len(string) else True

		end += 1

	return False

print(checkMe('leetcode', ['leet', 'code', 'me']))