# this demonstrates looping techniques

# for a sequence like list or tuple, to get both position and value
for i,v in enumerate(['apples', 'oranges', 'grapes']):
	print i, '-', v

# example of zipping
list1 = ['hey', 'boy', 'howdy']
list2 = [',yo!', 'girl', 'doing?']

for val1, val2 in zip(list1, list2):
	print '%r - %r' %(val1, val2)

for i in reversed(range(1,5)):
	print i

for i in sorted([3,1,5,3,10,9,6]):
	print i

dict = {'a': 1, 'b': 2, 'c': 3}
for i, v in dict.iteritems():
	print '%r - %r' %(i, v)
	
print (1, 2, 3, 4) < (1, 2, 4) #true because 3 < 4 and the comparison breaks