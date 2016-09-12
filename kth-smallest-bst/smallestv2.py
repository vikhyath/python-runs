class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.count = 0

class BST:
	def __init__(self):
		self.root = None

	def insert(self, val, node=None):
		if not self.root:
			self.root = Node(val)
			self.root.count = 1
			return

		if not node:
			node = self.root

		if val < node.val:
			node.count += 1
			if node.left is None:
				newNode = Node(val)
				newNode.count = 1
				node.left = newNode
				return
			self.insert(val, node.left)

		if val > node.val:
			if node.right is None:
				newNode = Node(val)
				newNode.count = 1
				node.right = newNode
				return
			self.insert(val, node.right)

	def in_order(self, node):
		if not node:
			return

		self.in_order(node.left)
		print(str(node.val) + ' : ' + str(node.count))
		self.in_order(node.right)

	def kthsmall(self, k, node, found=False):

		if not node:
			return found

		found = self.kthsmall(k, node.left, found)
		if found:
			return found

		self.ctr += 1

		if self.ctr == k:
			print(node.val)
			return True

		found = self.kthsmall(k, node.right, found)
		if found:
			return found

	def kthsamllopt(self, k, node):
		if not node:
			return

		if k == node.count:
			print(node.val)

		elif k < node.count:
			self.kthsamllopt(k, node.left)

		else:
			self.kthsamllopt(k - node.count, node.right)

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(2)
bst.insert(8)
bst.insert(7)
bst.insert(9)
bst.insert(15)

bst.in_order(bst.root)
bst.ctr = 0
bst.kthsmall(2, bst.root)
bst.ctr = 0
bst.kthsmall(5, bst.root)
bst.ctr = 0
bst.kthsmall(4, bst.root)
bst.ctr = 0
bst.kthsmall(7, bst.root)
bst.ctr = 0
bst.kthsmall(14, bst.root)
print('------------')
bst.kthsamllopt(2, bst.root)
bst.kthsamllopt(5, bst.root)
bst.kthsamllopt(4, bst.root)
bst.kthsamllopt(7, bst.root)
bst.kthsamllopt(14, bst.root)