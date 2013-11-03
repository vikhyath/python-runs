def square(x):
    return x**2

# comprehensions
list = [1,2,3,4]
list1 = [(x, y) for x in range(1,4) for y in range(1,4) if x != y] # using {x,y} creates a set([x, y]) for each x and y pair
print list1

stringlist = [' apple ', ' banana', 'rasberry ']
newslist = [word.strip() for word in stringlist]
print newslist

numsquare = [(x,x**2) for x in list]
print numsquare

dict1 = {x: square(x) for x in xrange(1,6)}
print dict1

del list[:]
print list