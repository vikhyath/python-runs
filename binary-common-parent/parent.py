# Given a forest of balanced binary trees and two nodes, n1 and n2, 
# find the closest common parent of n1 and n2. 
# Nodes have parameters "parent", "left" and "right", 
# and you cannot access the values of the nodes. 
# If n1 and n2 are not on the same tree, return NULL. 

# Try to do this in O(log(n)) time and O(1) space.

class Node:
	def __init__(self, val):
		self.val = val
		self.parent = None
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.val)

class Tree:
	def __init__(self):
		self.root = None

	def left(self, val, node):
		node.left = Node(val)
		node.left.parent = node
		return node.left

	def right(self, val, node):
		node.right = Node(val)
		node.right.parent = node
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

	def ancestor(self, node1, node2):
		# find root distance

		print(self.__findRoot(node1, node2))

	def __findRoot(self, node1, node2):
		ctr1 = 0
		ctr2 = 0
		node1Copy = node1
		node2Copy = node2
		while node1.parent or node2.parent:
			if node1.parent:
				ctr1 += 1
				node1 = node1.parent

			if node2.parent:
				ctr2 += 1
				node2 = node2.parent

		if node1 and node2 and node1 != node2:
			return 'diff mother'

		node1 = node1Copy
		node2 = node2Copy
		while ctr1 > ctr2:
			node1 = node1.parent
			ctr1 -= 1

		while ctr2 > ctr1:
			node2 = node2.parent
			ctr2 -= 1

		while(node1 != node2):
			node1 = node1.parent
			node2 = node2.parent

		# same route, then return parent
		if node1 == node2Copy:
			return node2Copy.parent if node2Copy.parent else node2Copy

		if node2 == node1Copy:
			return node1Copy.parent if node1Copy.parent else node1Copy

		return node1

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

node30 = Node(30)

tree.tree(tree.root)
tree.ancestor(node15, node1)
tree.ancestor(node, node8)
tree.ancestor(node5, node1)
tree.ancestor(node2, node19)
tree.ancestor(node8, node19)
tree.ancestor(node19, node25)

tree.ancestor(node8, node16)
