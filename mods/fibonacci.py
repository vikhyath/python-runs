# fibonacci numbers module
def fib_upto(n):
	a = 0
	b = 1
	while b <= n:
	  print b
	  temp = b
	  b = a+b
	  a = temp
	  
def fib_n(n):
	a, b, count = 0, 1, 0
	while count <= n:
	  print b
	  temp = b
	  b = a+b
	  a = temp
	  count = count + 1
	  
# check to see if it is being run as a script, if yes then call method. 
# if it is not being run as a script, and it is being run as a module. dont call method
if __name__ == '__main__':
  fib_upto(30)