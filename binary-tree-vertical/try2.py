from collections import deque

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None
		self.heights = {}
		self.queue = deque()
		self.order = deque()

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

	def real_vertical(self, node):
		if node:
			self.queue.append(node)
			self.order.append(0)

			while(len(self.queue)):
				node = self.queue.popleft()
				order = self.order.popleft()
				if order not in self.heights:
					self.heights[order] = []

				self.heights[order].append(node.val)
				if node.left:
					self.queue.append(node.left)
					self.order.append(order + 1)
				if node.right:
					self.queue.append(node.right)
					self.order.append(order - 1)

# Given a binary tree, print it vertically. The following example illustrates vertical order traversal.
#            1
#         /    \
#        2      3
#       / \    / \
#      4   5  6   7
#              \   \
#               8   9 
               
     
# The output of print this tree vertically will be:
# 4
# 2
# 1 5 6
# 3 8
# 7
# 9 

node = Node(1)
tree = Tree()

tree.root = node

node2 = tree.left(2, tree.root)
node3 = tree.right(3, tree.root)

node4 = tree.left(4, node2)
node5 = tree.right(5, node2)

node6 = tree.left(6, node3)
node7 = tree.right(7, node3)

node8 = tree.right(8, node6)

node9 = tree.right(9, node7)

tree.real_vertical(tree.root)
newheights = sorted(tree.heights.items(), key=lambda x: x[0], reverse=True)
for item in newheights:
	nodes = ','.join(map(str, item[1]))
	print(str(item[0]) + ': ' + nodes)

print('-------------------------------------')

node = Node(5)
tree = Tree()
tree.root = node

node1 = tree.left(1, tree.root)
node6 = tree.right(6, tree.root)

node3 = tree.right(3, node1)

node2 = tree.left(2, node3)
node4 = tree.right(4, node3)

tree.real_vertical(tree.root)
newheights = sorted(tree.heights.items(), key=lambda x: x[0], reverse=True)
nodesvertical = []
for item in newheights:
	nodesvertical.append(item[1])
print(nodesvertical)
print('-------------------------------------')