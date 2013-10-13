# list comprehensions
list = [1,2,3,4]
list1 = [(x, y) for x in range(1,4) for y in range(1,4) if x != y]
print list1

stringlist = [' apple ', ' banana', 'rasberry ']
newslist = [word.strip() for word in stringlist]
print newslist

numsquare = [(x,x**2) for x in list]
print numsquare

del list[:]
print list