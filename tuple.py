#usage of tuple
# http://getpython3.com/diveintopython3/native-datatypes.html#tuples

tuple = (3,4,5,6)
print tuple
tuple += (7,8)
print tuple



dict = {}
dict['banana', 'blue'] = 20
dict['apple', 'green'] = 10
print dict

for i,v in dict.iteritems():
	print i,v
	
print dict['banana', 'blue']

newfruits = ['biscuit', 'cookie', 'apple']
newsets = set(newfruits)
print 'cookie' in newsets

newsets = {1,2,'asd'}
print newsets

del newsets[1] #error, set does not support del
print newsets 