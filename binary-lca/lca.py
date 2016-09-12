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

	def find(self, node, val1, val2):
		if not node:
			return None

		if node.val == val1 or node.val == val2:
			return node.val

		leftFound = self.find(node.left, val1, val2)
		rightFound = self.find(node.right, val1, val2)

		if leftFound and rightFound:
			return node.val

		return leftFound if leftFound else rightFound

	def countlower(self, node):
		if not node:
			return 0

		count = 0
		if node.left and node.val > node.left.val:
			count += 1

		if node.right and node.val > node.right.val:
			count += 1

		leftCount = self.countlower(node.left)
		rightCount = self.countlower(node.right)

		return count + leftCount + rightCount

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

print(tree.find(tree.root, 19, 8))

print(tree.countlower(tree.root))

newtree = Tree()
node = Node(15)
newtree.root = node

node16 = newtree.left(16, newtree.root)
node5 = newtree.right(5, newtree.root)
new4 = newtree.right(4, node5)
print(newtree.countlower(newtree.root))