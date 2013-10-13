#more functions
def testparams(arg1, arg2):
	return arg1+arg2
	
#if __name__ == '__main__':
#  ret = testparams(1,2)
#  print 'sum of arg1 + arg2 is %d' %ret
#  if ret == 1:
#    print 'ret is 1'
#  elif ret == 2:
#     print 'ret is 2'
#   elif ret == 3:
#     print 'ret is 3'
#   else:
#     print 'ret is more than 3'

words = ['word1', 'word2', 'word3', 'word4']
for i in range(0, len(words)):
  print words[i]

wordscopy = words[:] # copy 

print wordscopy

arr = []
arr.append(2)
arr.insert(0,3)
print arr # [3,2]
  
# a[start:end] # items start through end-1
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array