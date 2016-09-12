# Given a list of unique words. Find all pairs of distinct indices 
# (i, j) in the given list, so that the concatenation of the two words,
#  i.e. words[i] + words[j] is a palindrome.

# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

words = ["abcd", "dcba", "lls", "s", "sssll", "abba", ""]

exists = {word: idx for idx, word in enumerate(words)}

res = []

def ispalin(word):
	if not len(word):
		return False

	return word == word[::-1]

if "" in exists:
	for word in words:
		if ispalin(word):
			res.append([exists[""], exists[word]])
			res.append([exists[word], exists[""]])

for widx, word in enumerate(words):
	for idx in range(len(word) + 1):
		if len(word[:idx]):
			if ispalin(word[:idx]):
				leftover = word[idx:]
				rev = leftover[::-1]
				if rev in exists and exists[rev] != widx and len(rev):
					res.append([exists[rev], exists[word]])

			rev = word[:idx][::-1]
			if rev in exists and exists[rev] != widx and len(rev) and \
				(not len(word[idx:]) or ispalin(word[idx:])):
				res.append([exists[rev], exists[word]])

		if ispalin(word[idx:]):
			leftover = word[:idx]
			if len(leftover):
				rev = leftover[::-1]
				if rev in exists and exists[rev] != widx and len(rev):
					res.append([exists[word], exists[rev]])

print(res)
