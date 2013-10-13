def listrev(list):
	print list
	for i in(xrange(len(list)-1, -1, -1)):
		yield list[i]

def main():
	for x in listrev('abcdefghij'):
		print x,

if __name__ == '__main__':
	main()

def add(x, y):
	return x+y

def decorate(func):
	def inner(x=2, y=3):
		return func(x,y)+1

	return inner

add = decorate(add)
print "\n",add(4,5)

def updatedict(old, new):
	old.update(new)

dict = {1: 'a', 2: 'b'}
updatedict(dict, {3: 'c', 4: 'd'})

print dict

listx = [0,1,2,3,4,5]
listx += [(6,7)]

setx = set(listx)
setx.update([8,9],[10,11])
setx.remove(1)
print setx

listy = [x for x in xrange(11)]
print listy

sety = set([1,2,(3,4)])
print sety
