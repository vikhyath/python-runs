# Given a linked list, reverse the nodes of a linked list k at 
# a time and return its modified list.

# If the number of nodes is not a multiple of k then left-out 
# nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself
#  may be changed.

# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# https://leetcode.com/problems/reverse-nodes-in-k-group/

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class List:
	def __init__(self, head):
		self.head = head

	def next(self, node, val):
		newnode = Node(val)
		node.next = newnode
		return newnode

	def reverse(self, node, k):
		j = k
		nodes = []
		while node is not None and j > 0:
			if node:
				nodes.append(node)

			node = node.next

			j -= 1
		
		if len(nodes) == k:
			ret = nodes[-1]
			switch = ret.next

			# now reverse
			prev = None
			while len(nodes):
				curr = nodes.pop()
				if prev:
					prev.next = curr
				prev = curr

			prev.next = switch

			got = self.reverse(switch, k)
			if got:
				prev.next = got

			return ret
		else:
			return None

	def printlist(self, node):
		while node:
			print(str(node.val) + ' -> ', end='')
			node = node.next

		print('')

one = Node(1)
alist = List(one)

two = alist.next(one, 2)

three = alist.next(two, 3)

four = alist.next(three, 4)

five = alist.next(four, 5)

six = alist.next(five, 6)

alist.printlist(alist.head)

alist.head = alist.reverse(alist.head, 2)

alist.printlist(alist.head)