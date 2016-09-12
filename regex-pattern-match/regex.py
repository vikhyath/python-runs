# https://leetcode.com/problems/regular-expression-matching/

# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

#!/usr/bin/env python

def match(string, reg):
	if not reg:
		return string is None or len(string) == 0

	dp = []

	for row in range(len(string)+1):
		dp.append([])
		for col in range(len(reg)+1):
			dp[row].append(False)

	dp[0][0] = True

	for col in range(1, len(dp[0])):
		idx = col - 1
		if reg[idx] == '*':
			if col - 2 >= 0:
				dp[0][col] = dp[0][col-2]

	for row in range(1, len(dp)):
		for col in range(1, len(dp[0])):
			s = string[row-1]
			p = reg[col-1]

			if p != '*':
				if s == p or p == '.':
					dp[row][col] = dp[row-1][col-1]

			else:
				if s != reg[col-2] and reg[col-2] != '.':
					dp[row][col] = dp[row][col-2]

				else:
					dp[row][col] = dp[row][col-2] or dp[row-1][col] or dp[row][col-1]


	print(dp[len(dp)-1][len(dp[0])-1])

# Some examples:
match("aa","a")
match("aa","aa")
match("aaa","aa")
match("aa", "a*")
match("aa", ".*")
match("ab", ".*")
match("aab", "c*a*b")

