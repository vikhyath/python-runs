# Given a forest of balanced binary trees and two nodes, n1 and n2, 
# find the closest common parent of n1 and n2. 
# Nodes have parameters "parent", "left" and "right", 
# and you cannot access the values of the nodes. 
# If n1 and n2 are not on the same tree, return NULL. 

# Try to do this in O(log(n)) time and O(1) space.

#!/usr/bin/env python

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None

	def __str__(self):
		return str(self.val)

class Tree:
	def __init__(self):
		self.root = None

	def left(self, val, pnode):
		node = Node(val)
		pnode.left = node
		node.parent = pnode
		return node

	def right(self, val, pnode):
		node = Node(val)
		pnode.right = node
		node.parent = pnode
		return node

	def tree(self, node):
		if not node:
			return
		if not node.left and not node.right:
			return
		print(str(node.val) + ' -> ', end='')


		if node.left:
			print(' L ' + str(node.left.val), end='')

		if node.right:
			print(' R ' + str(node.right.val), end='')

		print()
		self.tree(node.left)
		self.tree(node.right)

	def ancestor(self, node1, node2):
		# go to root, keep checking each other
		# if reached root and root is not same then diff mother
		# if each other check while going up is found then return found
		# calc distance, traverse up of lower count then go up simultaneously
		#    until parent is found

		node1copy = node1
		node2copy = node2
		node1dist = 0
		node2dist = 0

		if not node1 or not node2:
			print('null pointers')
			return

		while node1copy.parent:
			node1dist += 1
			if node1copy.parent == node2:
				print(node2)
				return

			node1copy = node1copy.parent

		while node2copy.parent:
			node2dist += 1
			if node2copy.parent == node1:
				print(node1)
				return

			node2copy = node2copy.parent

		if node1copy != node2copy:
			print('diff mom')
			return

		node1copy = node1
		node2copy = node2
		while node1dist > node2dist:
			node1copy = node1copy.parent
			node1dist -= 1

		while node2dist > node1dist:
			node2copy = node2copy.parent
			node2dist -= 1

		# now go up one node at a time until equal
		while node1copy != node2copy:
			node1copy = node1copy.parent
			node2copy = node2copy.parent

		if node1copy.parent:
			print(node1copy.parent)
		else:
			print(node1copy)

node = Node(10)
tree = Tree()

tree.root = node

node5 = tree.left(5, tree.root)
node1 = tree.left(1, node5)
node8 = tree.right(8, node5)
node15 = tree.right(15, tree.root)
node7 = tree.right(7, node15)
node2 = tree.left(2, node7)
node20 = tree.right(20, node7)
node25 = tree.right(25, node20)
node16 = tree.left(16, node20)
node9 = tree.left(9, node16)
node19 = tree.right(19, node16)

# tree.tree(tree.root)

newnode = Node(30)

tree.ancestor(node20, newnode)
tree.ancestor(node, node25)
tree.ancestor(node25, node9)
tree.ancestor(None, node9)
tree.ancestor(node1, node19)