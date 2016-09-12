# Given a string containing just the characters '(' and ')', 
# find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", 
# 	which has length = 2.

# Another example is ")()())", where the longest valid parentheses 
# substring is "()()", which has length = 4.

# https://leetcode.com/problems/longest-valid-parentheses/

#!/usr/bin/env python

def longest(string):
	stack = []
	left = -1

	maxi = 0
	totalmax = 0

	for idx in range(len(string)):
		char = string[idx]

		if char == '(':
			stack.append(idx)

		else:
			if not len(stack):
				left = idx
			else:
				top = stack.pop()
				if not len(stack):
					totalmax = max(totalmax, idx-left)
				else:
					totalmax = max(totalmax, idx-stack[-1])

	print(totalmax)

longest(')()())')
longest('(((')
longest('())))')
longest('()(()')
longest('(()')