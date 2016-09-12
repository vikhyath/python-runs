#!/usr/binenv python

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None
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

	def longest(self, node, count=1):
		isLeftBst = False
		isRightBst = False
		leftCount = 0
		rightCount = 0
		if not node:
			return count

		if node and node != self.root:
			if node.left and node.left.val < node.val:
				leftCount = 1
				isLeftBst = True
			elif not node.left:
				isLeftBst = True

			if node.right and node.right.val > node.val:
				rightCount = 1
				isRightBst = True

			elif not node.right:
				isRightBst = True

		count = count + leftCount + rightCount if isLeftBst and isRightBst else 1

		leftsubcount = self.longest(node.left, count)
		rightsubcount = self.longest(node.right, count)

		maxcount = count if count > leftsubcount else leftsubcount
		maxcount = maxcount if maxcount > rightsubcount else rightsubcount

		return maxcount
			

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

print(tree.longest(tree.root))