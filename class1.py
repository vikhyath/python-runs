# the file name does not need to match the class name like java
# the first argument to a method will be the object reference, this is useful for context identification inside the class
class Test:
	i = 10
	def hello(this):
		print 'hello %d' %this.i

obj = Test()
obj.i = 20
obj.hello()

obj1 = Test()
obj1.i = 30
obj1.hello()

# def __init__ is like the constructor, the method that will run in the class when an object is created

class TestAgain:
	name = None
	def __init__(self, string):
		self.name = string

	# def __init__(self, s1, s2): doing overloading will overwrite the previous init, that is python will always think that
	# __init__ is now going to be called with 3 arguments.
	#	self.name = s2
	def echo(self):
		print self.name

obj1 = TestAgain('object1')
obj1.echo()

obj2 = TestAgain('object2')
obj2.echo()

# obj3 = TestAgain('xyz', 'Overloading constructor not possible')
# obj3.echo()


def x():
	print 'this is x'

# note how y takes the method x
# not how init created a list within the context of self. now this init can be used from anywhere which has a self context
class TestMethods:
	y = x
	def __init__(self):
		print 'in TestMethods init'
		self.list = []
	def addtolist(self, list):
		for val in list:
			self.list.append(val)
	def printlist(self):
		print self.list
	def printx(self):
		print self.k # just x will give the function defined above

obj = TestMethods()
obj.y
obj.addtolist([1,2,3,4])
obj.printlist()

# inheritence
class NewTestMethods(TestMethods):
	k = 10
	def __init__(self):
		print 'in NewTestMethods init'
		# super(NewTestMethods, self).__init__() # should work in newer versions of python
		TestMethods.__init__(self)
		self.list = [] # this will be local to TestMethods object scope, hence it would be accessible in NewTestMethods

obj = NewTestMethods()
obj.addtolist([54,53,52])
obj.printlist()
obj.printx()
