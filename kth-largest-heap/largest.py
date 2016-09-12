#!/usr/bin/env python

import queue

q = queue.PriorityQueue()

alist = [5, 2, -2, 7, 0, 1, 4] # -2 0 1 2 4 5 7

size = 3

for item in alist:
	q.put(item)
	if q.qsize() == size:
		break

# now go over remaining items and check if q min is < next element
start = size
while(start < len(alist)):
	top = q.get()
	if top < alist[start]:
		q.put(alist[start])
	else:
		q.put(top)
	start += 1

print(q.get())
