# A decorator is just a callable that takes a function as an argument and returns a replacement function. 
# Decorators can be used to create wrapper functions which can be helpful in doing additional checks

def outer(some_func):
	print 'in outer'
	def inner():
		x = 2
		x = some_func(x) + 1
		return x
	return inner

def foo(x):
	print 'in foo'
	return 1

bar = outer(foo)
print bar()


# wrapper returns a decorated version  of add and sub

def sub(a, b):
	return a-b

def add(a, b):
	return a+b

def wrapper(func):
	def innercheck(a, b):
		if (a < 0):
			a = 0
		if (b < 0):
			b = 0
		retval = func(a, b)
		if (retval < 0):
			retval = 0
		return retval
	return innercheck

add = wrapper(add)
sub = wrapper(sub)

sumd = add(-1, -2)
diff = sub(3, 2)

print sumd
print diff

