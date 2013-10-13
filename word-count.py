
# counting the occurrance of each word
dict = {}
with open('input.txt', 'r') as f:
	for line in f:
		words = line.split()
		for word in words:
			if word in dict:
				dict[word] += 1
			else:
				dict[word] = 0

print dict

# will read all lines, each line will be stored as an element in the list
with open('input.txt', 'r') as f:
	print f.readlines()
	
# third way of reading, not so good because we need to handle clost operation etc.
fp = open('input.txt', 'r')
for singleline in fp:
	print singleline
fp.close()