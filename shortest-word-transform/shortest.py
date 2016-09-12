# Given a dictionary containing a list of words, a starting word,
#  and an ending word, return the minimum number of steps to transform 
#  the starting word into the ending word. 

# A step involves changing one letter at a time to a valid word that 
# is present in the dictionary. 

# Return null if it is impossible to transform the starting word into the ending word using the dictionary. 

# Example: 

# Starting word: cat 
# Ending word: dog 

# cat -> cot -> cog -> dog ('cot' and 'cog' are in the dictionary) 

# return 3

import string

def neighborFind(frm, dictionary, path=set()):
	neighbors = []
	for word in dictionary:
		if word == frm or word in path:
			continue
		idx = 0
		while idx < len(word):
			for char in list(string.ascii_lowercase):
				if word[:idx] + char + word[idx+1:] == frm:
					neighbors.append(word)
					break

			idx += 1

	return neighbors

def transform(start, end, dictionary, path=set()):
	if start == end:
		return [start]

	# create a copy to not mess up recursion path variable
	testpath = path.copy()
	testpath.add(start)

	neighbors = neighborFind(start, dictionary, testpath)
	maxPath = []
	for neighbor in neighbors:
		if neighbor == end:
			return [start, neighbor]
		else:
			isTherePath = transform(neighbor, end, dictionary, testpath)
			if len (isTherePath):
				isTherePath = [start] + isTherePath

			if len(isTherePath) and (len(maxPath) == 0 or len(isTherePath) < len(maxPath)):
				maxPath = isTherePath
	
	return maxPath

path = transform('cat', 'dog', 
	['cat', 'cot', 'dog', 'cog', 'mot', 'pot', 'col', 'bat', 'mat', 'rat', 'pat', 'cam'])

# path = transform('cat', 'dog', 
# 	['cat', 'bat', 'lat', 'lot', 'dot', 'bet', 'bed', 'at', 'ad', 'ed', 'cat', 'cog', 'dog', 'cot'])

print(path)


# def transform(start, end, dictionary, path=[]):
# 	if start not in path:
# 		path.append(start)

# 	if start == end:
# 		return [start]

# 	print('for: ' + start + ' ------------------------------- ' + str(path))

# 	neighbors = neighborFind(start, dictionary, path)
# 	print(neighbors)
# 	maxPath = []
# 	for neighbor in neighbors:
# 		if neighbor == end:
# 			path.append(neighbor)
# 			maxPath = []
# 			maxPath.append(start)
# 			maxPath.append(end)
# 			break
# 		else:
# 			isTherePath = transform(neighbor, end, dictionary, path)
# 			if len (isTherePath):
# 				isTherePath.insert(0, start)
# 				print('$$$$$$$ ' + str(isTherePath) + '')

# 			if len(isTherePath) or (not len(maxPath) and len(isTherePath) < len(maxPath)):
# 				print('found shorter path')
# 				maxPath = isTherePath
# 				print(maxPath)
# 			else:
# 				print('ignorning longer: ' + str(isTherePath))
# 				path.pop()

# 	print('sending back: ' + str(maxPath))
# 	return maxPath