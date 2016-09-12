#!/usr/binenv python

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None
		self.maxSoFar = 0
		pass

	def left(self, val, node):
		node.left = Node(val)
		return node.left

	def right(self, val, node):
		node.right = Node(val)
		return node.right

	def tree(self, node=None):
		if node and (node.left or node.right):
			print(str(node.val) + ' -> ', end='')
			if node.left:
	
				print(' L ' + str(node.left.val), end='')

			if node.right:
				print(' R ' + str(node.right.val))
			self.tree(node.left)
			self.tree(node.right)

	def longest(self, node):
		if not node:
			return 0

		isLeft = False
		isRight = False

		sumLeft = self.longest(node.left) if node.left else 0

		sumRight = self.longest(node.right) if node.right else 0

		isLeft = True if not node.left or node.val > node.left.val else False
		isRight = True if not node.right or node.val < node.right.val else False

		total = 1
		if isRight and isLeft:
			total += sumLeft + sumRight

		elif isRight or isLeft:
			if node.left and isLeft:
				total += sumLeft
			if node.right and isRight:
				total += sumRight

		if total > self.maxSoFar:
			self.maxSoFar = total

		return total

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


tree.tree(tree.root)

tree.longest(tree.root)
print(tree.maxSoFar)