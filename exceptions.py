try:
	with open('a.txt', 'r') as f:
		for line in f:
			print line
except IOError:
	print 'ok caught error'

# failing an import
try:
	import xyz
except ImportError as e:
	print 'importError'

# handling multiple
try:
	from collections import xyz
	fp = open('xyz', 'r')
except (ImportError, IOError): #note that this needs to be in () because in older versions python, except a, b: means except a as b:
	print 'caught both errors %'

# The try ... except statement has an optional else clause, which, when present, must follow all except clauses. 
# It is useful for code that must be executed if the try clause does not raise an exception. For example:

try:
	x = 1/0
except Exception:
	print 'zero div error'
else:
	print 'this will run if try throws no exception'
finally:
	print '''this will run after both the try (and else: if no exception is raised) or except runs, this will run before except
	if there was no matching class that could catch the except raised, which means that the exception will be raised after this
	runs'''