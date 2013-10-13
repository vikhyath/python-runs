x = ['foo', [1,2,3], 10.4]
y = list(x) # or x[:]
y[0] = 'fooooooo'
y[1][0] = 4
print x
print y

print type(x) is list #returns True

k = x[:] # this thing here makes a fresh new copy of the list in the object space and assigns it a variable k
z = x # this will make a variable z point to the same object that x is pointing to

# is will return true if two variables point to the same object
print k is x # returns False
print z is x # returns True

# == will return true if the objects pointed to by the variables are equal
print k == x # returns True