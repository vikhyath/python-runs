# does not work, misses a case with a starting *

# Implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a")  false
# isMatch("aa","aa") true
# isMatch("aaa","aa") false
# isMatch("aa", "*") true
# isMatch("aa", "a*") true
# isMatch("ab", "?*") true
# isMatch("aab", "c*a*b") false

# Understand the problem:
# The key of the problem is to understand the '*', which is able to match ANY sequence of characters. e.g. isMatch(abcd, *) -> true. Note that * does not require the same character in the sequence, as was required by the regular expression matching. 

def isMatch(word, regex):
	regIdx = 0
	wordIdx = 0
	match = True
	lastNonStar = 0
	while(wordIdx < len(word) and regIdx < len(regex) and match):
		char = regex[regIdx]
		wordChar = word[wordIdx]

		if wordChar == char or char == '?':
			wordIdx += 1
			regIdx += 1
			lastNonStar = regIdx

		elif char == '*':
			regIdx += 1

		# a new character
		else:
			if char in word[wordIdx:]:
				oldwordIdx = wordIdx
				wordIdx = word[wordIdx:].index(char)

				# advance wordIdx since we are looking in a subset of actual word so indeces will defer
				wordIdx = wordIdx + oldwordIdx
				# ensure there was a *
				if wordIdx - oldwordIdx > 0:
					if '*' not in regex[lastNonStar:regIdx]:
						match = False
					else:
						wordIdx += 1

				regIdx += 1

			else:
				match = False

	# if regex has ended
	if (match and regIdx == len(regex)):
		if len(regex) and regex[-1] == '*':
			match = True
		else:
			if wordIdx < len(word):
				match = False

	elif (match and wordIdx == len(word)):
		if len(regex) and regex[-1] != '*':
			match = False
		else:
			if regIdx < len(regex) and ''.join(set(regex[regIdx:])) != '*':
				match = False

	return match

print(isMatch("aa","a"))
print(isMatch("aa","aa"))
print(isMatch("aaa","aa"))
print(isMatch("aa", "*"))
print(isMatch("aa", "a*"))
print(isMatch("ab", "?*"))
print(isMatch("aab", "c*a*b"))
print(isMatch("abcd", "*"))
print(isMatch("abcgfeefeff*sd", "a*f*d"))
print(isMatch("", ""))
print(isMatch("", "a"))
print(isMatch("b", "*?*?*"))
print(isMatch("b", "*?*b*"))
print(isMatch("hi", "*?"))
print(isMatch("hia", "*?a"))




