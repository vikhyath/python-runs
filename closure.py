#example demonstrating closure

# an inner function that is not in global scope remembers what its enclosing namespace looked like at the time of function definition

def foo():
	c = 2
	def inner():
		# inner will first check its namespace to see if c is defined, since it is not, it looks at its enclosing namepsace
		# even though foo() returns, the context of c is not lost because the inner function remembers it
		print c
	return inner


bar = foo()
bar()

