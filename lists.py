# operations on a list datastructure, lists are very efficient to be used as a stack
# lists are inefficient to be used as queue, because all elements will have to be shifted left by 1
# hence for queue's use the deque method from collections

list = []
list.append(5)
list.append(4)
list.append(3)

print list

print 'popped:', list.pop()
print 'popped:', list.pop()

print list

list.insert(2,3)

print len(list)

# start with len and make slice till the end and copy the new list into current list
list[len(list):] = [4]
print list

# list.remove(45) # will throw an error because 45 is not present in the list

print list.index(4) # prints index of 4

print list.count(4)

list.sort()

print list

list.reverse()

print list