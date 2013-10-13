# modified binary search
list = [1,2,3,4,5,6,7,10,9,8]
start = 0
end = len(list)-1

def find(list, start, end, search):
	index = (start+end)/2
	if (list[index] == search):
		print 'element', search, ' found at', index
		return
	if start >= end:
		print 'element ', search, ' not found'
		return
	if (list[index] > search and index < end and index > start):
		if (list[index-1] >= search):
			print 'going left 3 with list[index]', list[index]
			find(list, start, index-1, search)
		else:
			print 'going right 3 with list[index]', list[index]
			find(list, index+1, end, search)
	elif (list[index] < search and index < end and list[index] < list[index+1]):
		print 'going right 1 with list[index]', list[index]
		find(list, index+1, end, search)
	elif (list[index] < search and index > start and list[index] < list[index-1]):
		print 'going left 1 with list[index]', list[index]
		find(list, start, index-1, search)
	elif (list[index] > search and index < end and list[index] > list[index+1]):
		print 'going right 2 with list[index]', list[index]
		find(list, index+1, end, search)
	elif (list[index] > search and index < end and list[index] < list[index+1]):
		print 'going left 2 with list[index]', list[index], start, index-1
		find(list, start, index-1, search)

for i in range(14,-2,-1):
	find(list, start, end, i)