# different ways of calling functions
# also an example to know how to import modules from diff directory

from sys import path
path.append('./mods')
import fibonacci as fib

# bad because we need to unpack stuff
def first_kind(*args):
	arg1, arg2 = args
	print "we got %r and %r in first kind" %(arg1, arg2)

# better because no unpacking needed, hence more clarity
def second_kind(arg1, arg2):
	print "we got %r and %r in the second kind" %(arg1, arg2)

def third_kind(arg1):
	print "trying for an error here",;print'got no error :(';

if __name__ == '__main__':
  first_kind(1,2)
  second_kind(3,4)
  third_kind(5)
  fib.fib_upto(20)

# is x is bound to an immutable object like a tuple or an integer or a string, 
# then the func will create a copy of the object pointed by x and point x to it
# where as if x is mutable like a list then both x and y point to the same list and 
# changes by x to the list are visible outside too. That is why python is neither
# call by value or call by ref, it is **** call by object reference ****

# no change to y outside the scope of this func
def test1(x):
	x += 1
	print x

y = 5
test1(y)
print y

def test2(y):
	y.append(3)
	return

y = [1,2]
print y
test2(y)
print 'after calling func, the list is:',y