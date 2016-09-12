# GIven a string "str" and pair of "N" swapping indices, 
# generate a lexicographically largest string. 
# Swapping indices can be reused any number times. 

# Eg 1) 

# String = "abdc" 

# Indices: 

# (1,4) 

# (3,4) 

# Answer: 

# cdba, cbad, dbac,dbca 

# should print only dbca which is lexicographically largest

# Example:

# "acxrabdz"
# Swaps allowed(0 based index) :-
# (0,2)(5,7)(2,7),(1,6)

strings = {}
string = "acxrabdz"
for idx, s in enumerate(string):
	strings[idx] = s

indices = [(0, 2), (5, 7), (2, 7), (6, 1)]

indices = list(sorted(indices, key=lambda x: x[0]))
print(indices)
graph = {}
collections = []

# if a graph dict can be used, this will improve to O(n)
for index in indices:
	if not len(collections):
		collections.append(set([index[0]] + [index[1]]))
		continue

	found = False
	for col in collections:
		if index[0] in col or index[1] in col:
			col.add(index[0])
			col.add(index[1])
			found = True
			break

	if not found:
		collections.append(set([index[0]] + [index[1]]))

print(collections)

for col in collections:
	strs = []
	for idx in col:
		strs.append(string[idx])

	strs = sorted(strs, reverse=True)
	ctr = 0
	for idx in col:
		strings[idx] = strs[ctr]
		ctr += 1

print(strings)

