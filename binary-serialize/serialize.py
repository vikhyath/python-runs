class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None
		self.heights = {}
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

	def serialize(self, node, nodestr=''):
		if not node:
			nodestr += 'null,'
			return nodestr

		nodestr += str(node.val) + ','
		nodestr = self.serialize(node.left, nodestr)
		nodestr = self.serialize(node.right, nodestr)

		return nodestr

	def deserialize(self, queue):
		val = queue.popleft()

		if val == 'null':
			return None

		node = Node(int(val))
		node.left = self.deserialize(queue)
		node.right = self.deserialize(queue)

		return node

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
nodestr = tree.serialize(tree.root)
print(nodestr)

from collections import deque
queue = deque()
for val in nodestr.split(','):
	if len(val):
		queue.append(val)

print(queue)

newtree = Tree()
newtree.root = newtree.deserialize(queue)

newtree.tree(newtree.root)

testree = Tree()
nodestr = testree.serialize(testree.root)
print(nodestr)

queue = deque()
for val in nodestr.split(','):
	if len(val):
		queue.append(val)

print(queue)
newtree = Tree()
newtree.root = newtree.deserialize(queue)

newtree.tree(newtree.root)