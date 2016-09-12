# Given two sorted linked lists of integers write an algorithm 
# to merge the two linked lists such that the resulting linked 
# list is in sorted order. You are expected to define the data 
# structure for linked list as well. Analyze the time and space 
# complexity of the merge algorithm.

#!/usr/bin/env python

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LL:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, val):
		if not self.head:
			self.head = Node(val)
			self.tail = self.head

		else:
			node = Node(val)
			self.tail.next = node
			self.tail = node

	def printlist(self):
		head = self.head
		while head:
			print(str(head.val) + ' -> ', end='')
			head = head.next

		print()

def merge(list1node, list2node):
	if not list1node and not list2node:
		return None

	elif not list1node:
		return list2node

	elif not list2node:
		return list1node

	else:
		newnode = Node(None)
		if list1node.val < list2node.val:
			newnode.val = list1node.val
			newnode.next = merge(list1node.next, list2node)
		else:
			newnode.val = list2node.val
			newnode.next = merge(list1node, list2node.next)

	return newnode

llist1 = LL()
llist1.insert(4)
llist1.insert(8)
llist1.insert(12)
llist1.insert(19)
llist1.printlist()

llist2 = LL()
llist2.insert(2)
llist2.insert(4)
llist2.insert(10)
llist2.insert(29)
llist2.printlist()

newnode = merge(llist1.head, llist2.head)
list3 = LL()
list3.head = newnode
list3.tail = newnode

list3.printlist()
