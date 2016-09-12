# Implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false

def matcher(string, p):
	if len(p) == 0:
		return len(string) == 0

	match = [[0 for i in range(len(p) + 1)] for j in range(len(string) + 1)]

	for i in range(len(string) + 1):
		match[i][0] = 0

	match[0][0] = 1

	for i in range(1, len(p) + 1):
		if p[i-1] == '*':
			match[0][i] = match[0][i-1]

	for i in range(1, len(string) + 1):
		for j in range(1, len(p) + 1):
			if p[j-1] != '*':
				if p[j-1] == string[i-1] or p[j-1] == '?':
					match[i][j] = match[i-1][j-1]
			else:
				match[i][j] = match[i-1][j-1] or match[i][j-1] or match[i-1][j]

	return match[len(string)][len(p)]

print(matcher("aa","aa"))
print(matcher("aaa","aa"))
print(matcher("aa", "a*"))
print(matcher("aa", "a*"))
print(matcher("ab", "?*"))
print(matcher("aab", "c*a*b"))