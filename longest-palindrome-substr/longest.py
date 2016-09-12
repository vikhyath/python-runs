# Given a string S, find the longest palindromic substring in S.
#  You may assume that the maximum length of S is 1000, and there 
#  exists one unique longest palindromic substring.

# https://leetcode.com/problems/longest-palindromic-substring/

#!/usr/bin/env python

def longest(string):
	if not len(string):
		return 0

	if len(string) == 1:
		return string

	idx = 0
	maxlen = 0
	minstart = 0
	minend = 0
	while idx < len(string):
		start = idx
		end = idx

		# skip dup chars
		while end < len(string) - 1 and string[end+1] == string[end]:
			end += 1

		# move idx to next
		idx = end + 1

		# now expand
		while start > 0 and end < len(string) - 1 and \
			string[start - 1] == string[end + 1]:
				start -= 1
				end += 1

		if maxlen < end - start + 1:
			maxlen = end - start + 1
			minstart = start
			minend = end

	print(string[minstart:minend+1])

longest('adbabdx')
longest('ccd')