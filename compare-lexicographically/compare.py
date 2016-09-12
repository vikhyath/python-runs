# Provide a function that allow to compare two strings lexicography, 
# having in mind that these words may contain digraphs 
# (two letters together represents a single one 
# i.e in Spanish ch is a single character ). 
# This in order to be able to sort a list of words.

# assumptions
# x = "abcdef"
# y = "abchef"

# i/p -> prolly an array with letters

def lexicals():
	return ['s', 'a', 'b', 'ch', 'c', 'd', 'e', 'f']

def compare(str1, str2):
	if len(str2) and not len(str1):
		return str1

	if len(str1) and not len(str2):
		return str2

	if not len(str1) and not len(str2):
		return None

	jack = 0
	jill = 0

	while (jack < len(str1) and jill < len(str2)):
		digraphStr1 = str1[jack]
		digraphStr2 = None
		if jack + 1 < len(str1):
			digraphStr1 = str1[jack] + str1[jack + 1]
			try:
				lexicals().index(digraphStr1)
				jack += 1
			except ValueError:
				digraphStr1 = str1[jack]
			
		if jill + 1 < len(str2):
			digraphStr2 = str2[jill] + str2[jill + 1]
			try:
				lexicals().index(digraphStr2)
				jill += 1
			except ValueError:
				digraphStr2 = str2[jill]


		# print(digraphStr1 + ': ' + str(lexicals().index(digraphStr1)))
		# print(digraphStr2 + ': ' + str(lexicals().index(digraphStr2)))
		if lexicals().index(digraphStr1) == lexicals().index(digraphStr2):
			pass

		elif lexicals().index(digraphStr1) < lexicals().index(digraphStr2):
			return str1

		else:
			return str2

		jack += 1
		jill += 1

	if jack == len(str1) and jill < len(str2):
		return str1

	if jill == len(str2) and jack < len(str1):
		return str2

	if jack == len(str1) and jill == len(str2):
		return str1 + ' and ' + str2

print(compare("abcde", "abche"))
print(compare("abcde", ""))
print(compare("", ""))
print(compare("abcdec", "abcdech"))