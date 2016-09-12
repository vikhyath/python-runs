# Given preorder traversal of a binary search tree, construct the BST.

# For example, if the given traversal is {10, 5, 1, 7, 40, 50}, 
# then the output should be root of following tree.

#      10
#    /   \
#   5     40
#  /  \      \
# 1    7      50  

#!/usr/bin/env python

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self, root):
		self.root = None

	def reconstruct(self, values):
		if not len(values):
			return

		stack = []
		val = values.pop(0)
		node = Node(val)
		self.root = node
		stack.append(node)

		while True:
			if not len(values):
				break

			top = stack.pop()
			nextval = values.pop(0)
			node = Node(nextval)

			if nextval < top.val:
				stack.append(top)
				top.left = node
				stack.append(node)
				continue

			preTop = top
			while len(stack) and nextval > top.val:
				preTop = top
				top = stack.pop()

			if nextval < top.val:
				stack.append(top)
			else:
				preTop = top

			preTop.right = node
			stack.append(node)

	def tree(self, node=None):
		if node and (node.left or node.right):
			print(str(node.val) + ' -> ', end='')
			if node.left:
	
				print(' L ' + str(node.left.val), end='')

			if node.right:
				print(' R ' + str(node.right.val))
			self.tree(node.left)
			self.tree(node.right)

tree = Tree(None)
tree.reconstruct([10, 5, 1, 7, 40, 50])
tree.tree(tree.root)

