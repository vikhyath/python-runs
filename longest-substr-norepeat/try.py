# Given a string, find the length of the longest substring without 
# repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence
#  and not a substring.

#!/usr/bin/env python

def longest(string):
	if not string or len(string) == 0:
		return 0

	start = 0
	end = 0
	mapped = {}
	count = 0
	while end < len(string):
		if string[end] in mapped:
			start = max(start, mapped[string[end]] + 1)

		mapped[string[end]] = end
		end += 1
		count = max(count, end-start)

	print(count)

longest("pwwkews")

longest("bxwxbcdef")