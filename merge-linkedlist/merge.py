#!/usr/bin/env python

class LinkedList:
	def __init__(self):
		self.root = None

	def next(self, fr, val):
		node = Node(val)
		if not self.root:
			self.root = node
		else:
			fr.next = node

		return node

	def show(self):
		node = self.root
		while(node):
			print(str(node.val) + ' -> ', end='')
			node = node.next

		print('')

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

ll = LinkedList()
node5 = ll.next(None, 5)
node8 = ll.next(node5, 8)
node14 = ll.next(node8, 14)
node18 = ll.next(node14, 18)

ll.show()

ll2 = LinkedList()
node2 = ll2.next(None, 2)
node6 = ll2.next(node2, 6)
node13 = ll2.next(node6, 13)
node20 = ll2.next(node13, 20)

ll2.show()

lr1 = ll.root
lr2 = ll2.root

llc = LinkedList()
node = None
while (lr1 or lr2):
	# if not lr1 or lr1.val > lr2.val:
	# 	print(str(lr2.val) + ' -> ', end='')
	# 	lr2 = lr2.next
	# elif not lr2 or lr2.val > lr1.val:
	# 	print(str(lr1.val) + ' -> ', end='')
	# 	lr1 = lr1.next
	
	if not lr1 or lr1.val > lr2.val:
		node = llc.next(node, lr2.val)
		lr2 = lr2.next
		ll2.root = lr2
	else:
		node = llc.next(node, lr1.val)
		lr1 = lr1.next
		ll.root = lr1

llc.show()
ll.show()
ll2.show()
