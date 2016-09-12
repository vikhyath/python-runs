# Given a string, determine if a permutation of the string could form a palindrome.
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.

def palindrome(string):
	length = len(string)
	if length == 1:
		return False

	# sum of all counts
	count = {}
	for char in string:
		count[char] = 1 if char not in count else count[char] + 1

	# if length is even, then make sure all chars occur even # times
	palin = True
	if length % 2 == 0:
		for char, cnt in count.items():
			if cnt % 2 > 0:
				return False
				break

	else:
		seenOdd = False
		for char, cnt in count.items():
			if cnt % 2 > 0:
				if seenOdd:
					return False

				else:
					seenOdd = True

	return palin

print(palindrome("code"))
print(palindrome("aab"))
print(palindrome("carerac"))
print(palindrome(""))
print(palindrome("a"))
print(palindrome("aabbccd"))
