

# O(n^2)
# abcbbbbcccbdddadacb
def longestn2(string):
	if len(string) < 2:
		return 0
		
	somedict = {}
	unique = 0
	length = 0
	idx = 0
	backidx = 0
	while(idx < len(string)):
		val = string[idx]

		if len(somedict.keys()) == 1:
			backidx = idx

		if len(somedict.keys()) < 2:
			somedict[val] = 1
			length += 1

		elif len(somedict.keys()) == 2:
			# adding this key will make it 3
			if val not in somedict:
				unique = unique if unique > length else length
				somedict = {}
				length = 0
				idx = backidx
				continue

			else:
				length += 1

		idx += 1

	unique = unique if unique > length else length
	return unique

# O(n) solution
def longestn(string):
	if len(string) < 2:
		return 0

	somedict = {}
	idx = 0
	cleanup = 0
	longest = 0
	unique = 0
	while(idx < len(string)):
		val = string[idx]

		if len(somedict.keys()) <= 2:
			if val not in somedict:
				unique = unique if unique > longest else longest
				somedict[val] = 1
			else:
				somedict[val] += 1

			longest += 1

		while(len(somedict.keys()) > 2 ):
			somedict[string[cleanup]] -= 1
			if somedict[string[cleanup]] == 0:
				del(somedict[string[cleanup]])
			cleanup += 1
			longest -= 1


		idx += 1

	unique = unique if unique > longest else longest
	return unique

print(longestn2("ecedba"))
print(longestn2("ecedcccecccddcba"))
print(longestn2(""))
print(longestn2("abcbbbbcccbdddadacb"))
print(longestn2("ab"))
print(longestn2("a"))
print(longestn2("aabaaddaa"))


print(longestn("ecedba"))
print(longestn("ecedcccecccddcba"))
print(longestn(""))
print(longestn("abcbbbbcccbdddadacb"))
print(longestn("ab"))
print(longestn("a"))
print(longestn("aabaaddaa"))