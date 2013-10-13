# A generator looks like a normal function but it returns an iterator. It has a special statement called yield that lets you
# return values from the function (usually for producing a series of values). At the same time it also suspends the current context, remembers it and then starts running
# from where it left of when next() is called.

# Advantages of using generators are that 
# 1) it remembers context, so you dont have to store self.index self.data etc
# 2) it also automatically creates the __iter()__ and next() methods
# 3) it raises StopIteration whenver the loop breaks

# A generator expression is similar to a list comprehension. It is a compressed form of a generator. The diff between list
# comprehension and generator expression is that a gen exp is enclosed in paranthesis. paranthesis are options if it is the
# only single argument that is being passed

# simple generators
def func(list):
	for val in list:
		yield val

def reverse(start, end):
	for val in xrange(end, start-1, -1):
		yield val

def reversestring(data):
	for char in xrange(len(data)-1, -1, -1): # start from len-1, include 0 and increment in -1 count
		yield data[char]

for e in func([1,2,3,4,5]):
	print e

print '\n'
for e in reverse(3, 5):
	print e 
print '\n'

for e in reversestring('abcdefg'):
	print e

# generator epressions
print sum(x*x for x in xrange(1, 4)) #sum of squares from 1 through 3 (1 + 4 + 9 = 14)

# dict example, dont know if this can be called a generator
# dict = {x:x+1 for x in [1, 2, 3]}
# print dict

list1 = [1,2,3]
list2 = [4,5,6]
ret = (x*y for x,y in zip(list1, list2)) #cross product. When we zip each element is a tuple, in this case
										 # it is (1, 4) (2, 5) (3, 6)
print ret.next() #4
print ret.next() #10
print ret.next() #18

ret = list(x*y for x,y in zip(list1, list2))
print ret

from math import pi, sin
ret = dict((x, sin(x*pi/180)) for x in range(0, 91))
print ret

ret = set((x,y) for x in [1,2,3] for y in [4,5,6])
print sorted(ret)