class StaticTest:
	count = 0
	def __init__(self):
	 	StaticTest.count += 1
	@staticmethod	# this is a decorator here
	def display():  # note the missing self
			print StaticTest.count

obj1 = StaticTest()
obj2 = StaticTest() 
StaticTest.display()

# note that list[] will remain same but never re-initialzed for each function call, that is because when def statement 
# executes, it takes some ready made pieces (including the compiled code of the current method and namespace) and create a
# function object, during this process it will also evaluate the default values assigned

# if we really want a fesh copy of list each time, we can re execute def each time to reinitialize

def ArgTest(list=[], a=5):
	list.append(a)
	return list

list = ArgTest(a=1)
print list
list = ArgTest(a=2)
print list
list = ArgTest(a=3)
print list
list = ArgTest(a=7)
print list

list = ArgTest([-1,-2,-3], a=4) # now this will override list and not use its default value
print list

# same concept with dictionaries too, in fact same concept will all mutables
# mutable object as a default value - that is, a value that can be modified in place, like a list or a dictionary.
def ArgTestNew(dict={}, a=2):
	dict[a] = a
	return dict

dict = ArgTestNew(a=1)
print dict
dict = ArgTestNew(a=2)
print dict
dict = ArgTestNew(a=3)
print dict

# ok now how to overcome this awesome problem?
# instead of setting list=[] do list = None. And initialize list=[] every time the method is called
def ArgModifiedTest(list=None, a=2):
	if list is None:
		list = []
	list.append(a)
	return list


list = ArgModifiedTest(a=1)
print list
list = ArgModifiedTest(a=2)
print list
list = ArgModifiedTest(a=3)
print list
