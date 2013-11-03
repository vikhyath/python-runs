# an iterator object confines to the iterator protocol, which basically means 2 methods are provided
# 1) __iter__(self) which is implicitly called at the beginning of loop
# 2) next() which is called for each loop iteration
# The StopIteration exception is implicity handled 

class ReverseList:
	def __init__(self, list):
		print 'initializing class'
		self.list = list
		self.count = 0
	def __iter__(self):
		return self
	def next(self):
		if self.count == len(self.list):
			raise StopIteration
		else:
			self.count += 1
			return self.list[len(self.list)-self.count]

obj = ReverseList([3,4,5,6, '-a'])
for c in obj:
	print c