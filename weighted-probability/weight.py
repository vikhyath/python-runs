# +-----------------+
# | fruit  | weight |
# +-----------------+
# | apple  |   4    |
# | orange |   2    |
# | lemon  |   1    |
# +-----------------+
# I need to return random fruit. But apple should be picked 
# 4 times frequently then lemon and 2 times frequently then orange.

# In more general case it should be f(weight) times frequently.

#!/usr/bin/env python

# A file contains strings like abcd 3.0 xyx 4.0 foobar 5.0
#  return random string but probability should be based on weighted 
#  averag

import random
string = 'abcd 3.0 xyx 4.0 foobar 5.0'
counts = []
something = {}
summer = 0
word = None
for idx, val in enumerate(string.split(' ')):
	# this is a word
	if idx % 2 == 0:
		word = val

	# insert this val times
	else:
		val = int(float(val))
		for i in range(0, val):
			counts.append([i+summer, word])
			something[i+summer] = word
		summer += val

rand = random.randint(0, summer-1)
print(counts[rand][1])

print(something[rand])