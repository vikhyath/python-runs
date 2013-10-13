# this demonstrates the uses of set data structure
# Python also includes a data type for sets. 
# A set is an unordered collection with no duplicate elements. 
# Basic uses include membership testing and eliminating duplicate entries. 
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
# 
# Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; 
# the latter creates an empty dictionary, a data structure that we discuss in the next section.
# 
# Here is a brief demonstration:

fruits = ['apple', 'banana', 'banana', 'pear', 'grape']
fruits.reverse()
print fruits

sets = set(fruits)


if 'apple' in sets:
   print 'yes in set'

print len(sets) #4

newfruits = ['biscuit', 'cookie', 'apple']
newsets = set(newfruits)

print newsets & sets #print common stuff INTERSECTION
print newsets | sets #print UNION
print newsets ^ sets #XOR, either in x or y but not both
print newsets - sets #DIFFERENCE

charset = set('aasdafsaffdfsdfdsfngirmnign') #cannot give 2 args, if 2 args needed give a list
print charset #prints unique chars

#like list comprehensions we can also do set comprehensions
x = {x for x in 'abcdefgh' if x not in 'abc'}
x.update('x', 'y') #adding new elements to the set in bulk
x.add('z') #adding one at a time
x.update(range(11))
print x

print dict['banana', 'blue']

newfruits = ['biscuit', 'cookie', 'apple']
newsets = set(newfruits)
print 'cookie' in newsets

newsets = {1,2,'asd'}
print newsets
