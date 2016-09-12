# Given a string, find the length of the longest substring without 
# repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence
#  and not a substring.

#!/usr/bin/env python

############################# WRONG #############################

# bug in tracking start index, it should be the max of last start and new start
# check try.py

def longest(string):
	if not len(string):
		return 0

	start = 0
	end = 0
	maxlen = 0
	track = {}

	while end < len(string):
		if string[end] in track:
			start = track[string[end]] + 1

		track[string[end]] = end
		maxlen = max(maxlen, end-start+1)
		end += 1

	print(maxlen)

longest("pwwkews")


