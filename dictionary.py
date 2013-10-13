#demonstrates the uses of a dictionary
# Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys,
# which can be any immutable type; strings and numbers can always be keys. 
# Tuples can be used as keys if they contain only strings, numbers, or tuples; 
# if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
# You cant use lists as keys since lists can be modified in place using index assignments
# slice assignments, or methods like append() and extend().

# It is best to think of a dictionary as an unordered set of key: value pairs, 
# with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. 
# Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; 
# this is also the way dictionaries are written on output.

dict = {'a': 1, 'b': 2, 'c': 3}
print dict
print 'a' in dict
dict['d'] = 4
print dict

for key in dict.keys(): #dict.keys() will return all keys in the dictionary
  print dict[key]
  
for value in dict.values(): #dict.values() will return all values in the dictionary
  print value

del dict['a'] #delete 'a'
print dict

newdict = {x:x*2 for x in range(1,4)}
print newdict

# example to demonstrate sorting
import operator
dict = {'a': 1, 'b': 3, 'c': 4}
newdict = sorted(dict.items(), key=operator.itemgetter(1, 0))  # technically it means sort by value then key
print newdict

#another way of doing this
newdict = sorted(dict.items(), key=lambda x: (x[1], x[0]))
print newdict

#sortin list
list = [('a',2),('a',1),('b',3),('c',4)]
sortedlist = sorted(list, key=operator.itemgetter(1,0), reverse=True) #do it in reverse
print sortedlist

print dict.keys()
print dict.values()