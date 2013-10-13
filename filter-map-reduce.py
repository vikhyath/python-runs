# this demonstrates uses of filter, map and reduce methods
list = []
list[len(list):] = range(1,10)
listcopy = list[:]
print list

def f(x):
	return x%2 == 0 and x%3 == 0

list = filter(f, list)

print list

newlist = range(1,3)

# map will call the function for each element in the list/lists set
def cube(x, y):
	if y!= None:
		return x*y
	else:
		return x*x*x

listcopy = map(cube, listcopy, newlist)
print listcopy

# reduce will, for the elements in the list, take two at a time and perform the operation that function specifies
# you can also have a third argument that is the starting value, if given then starval+first-element is first performed and
# then the rest
def red(x,y):
	return x+y

listcopy = reduce(red, listcopy)
print listcopy