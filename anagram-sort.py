# NOT EFFICIENT: finding anagrams, has duplicates and we maintain a list

list = ['hey', 'abcd', 'dcba', 'zyx', 'xyz', 'egf', 'yeh', 'ehy']

def checkanagram(x, y):
	return cmp(sorted(x), sorted(y))

anaglist = []

for i,v in enumerate(list):
	for j, w in enumerate(list):
		if v == w:
			continue
		result = checkanagram(v, w)
		if result == True:
			anaglist.append((v,w))
		print 'checking %s and %s: ' %(v, w),result

print list
print anaglist


list = sorted(list, cmp=checkanagram)
print list


# EFFICIENT: finding anagrams has no duplicate and we maintain a dict

list = ['abcd', 'a', 'ab', 'dec', 'dcba', 'ba', 'badc']
list = sorted(list, key=lambda x: sorted(x) )
print list

def func(v, parlist):
    anagrams = []
    for i, val in enumerate(parlist):
        if sorted(val) == sorted(v):
            anagrams.append(val)
    return anagrams

dict = {}
for i, v in enumerate(list):
    if ''.join(sorted(v)) not in dict:
        dict[v] = func(v, list[i+1:])

print sorted(dict.iteritems(), key=lambda (x,y): sorted(x))