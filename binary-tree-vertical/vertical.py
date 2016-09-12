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

# also calculate height of tree, if a tree A is a subtree of tree B and if a tree is a mirror of itself
#!/usr/binenv python

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

	def vertically(self, level, node=None):
		if node:
			if not level in self.heights:
				self.heights[level] = []
			self.heights[level].append(node.val)
		else:
			return

		self.vertically(level+1, node.left)
		self.vertically(level-1, node.right)


	def height(self, node):
		if not node:
			return 0

		return (1 + max(self.height(node.left), self.height(node.right)))
	
	def _identical(self, nodeA, nodeB):
		if not nodeB:
			return True

		if not nodeA:
			return False

		return (nodeA.val == nodeB.val and self._identical(nodeA.left, nodeB.left) and self._identical(nodeA.right, nodeB.right))


	def compare(self, nodeA, nodeB):
		if not nodeB:
			return True

		if not nodeA:
			return False

		if nodeA.val == nodeB.val:
			return self._identical(nodeA, nodeB)

		else:
			return self.compare(nodeA.left, nodeB) or self.compare(nodeA.right, nodeB)


	def mirror(self, nodeA, nodeB):
		if not nodeA and not nodeB:
			return True

		if not nodeA or not nodeB:
			return False

		return nodeA.val == nodeB.val and self.mirror(nodeA.left, nodeB.right) \
			and self.mirror(nodeA.right, nodeB.left)

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

sevennode = Node(7)
newTree = Tree()
newTree.root = sevennode
node2 = newTree.left(2, sevennode)
node20 = newTree.right(20, sevennode)
node16 = newTree.left(16, node20)
node25 = newTree.right(25, node20)

# newTree = Tree()
# tenNode = Node(10)
# newTree.root = tenNode
# fiveNode = newTree.left(5, tenNode)
# fifteenNode = newTree.right(15, tenNode)

tree.vertically(0, tree.root)

print(tree.heights)

print(tree.height(tree.root))

print(tree.compare(node, sevennode))

tenNode = Node(10)
mTree = Tree()
mTree.root = tenNode

twentyLeft = mTree.left(20, tenNode)
twentyRight = mTree.right(20, tenNode)
fiftyLeft = mTree.left(50, twentyLeft)
fiftyRight = mTree.right(50, twentyRight)
sixtyLeft = mTree.right(60, twentyLeft)
sixtyRight = mTree.left(60, twentyRight)
eightyRight = mTree.right(80, fiftyRight)

print(mTree.mirror(twentyLeft, twentyRight))