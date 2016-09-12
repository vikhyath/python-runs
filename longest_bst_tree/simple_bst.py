class Node:
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None


class BST:
	def __init__(self):
		self.root = None
		pass

	def insert(self, val):
		node = Node(val)
		self._find_and_insert(node, self.root)

	def _find_and_insert(self, node, head):
		if not self.root:
			self.root = node
			return

		if node.val < head.val:
			if not head.left:
				head.left = node
			else:
				self._find_and_insert(node, head.left)

		elif node.val == head.val:
			return False

		else:
			if not head.right:
				head.right = node
			else:
				self._find_and_insert(node, head.right)

	def pre_order(self, head):
		if head:
			print(head.val)

		else:
			return

		if head.left:
			self.pre_order(head.left)

		if head.right:
			self.pre_order(head.right)

	def in_order(self, head):
		if head and head.left:
			self.in_order(head.left)

		if head:
			print(head.val)

		if head and head.right:
			self.in_order(head.right)

	def post_order(self, head):
		if head and head.left:
			self.post_order(head.left)

		if head and head.right:
			self.post_order(head.right)

		if head:
			print(head.val)


bst = BST()
bst.insert(25)
bst.insert(15)
bst.insert(50)
bst.insert(10)
bst.insert(22)
bst.insert(35)
bst.insert(70)
bst.insert(4)
bst.insert(12)
bst.insert(18)
bst.insert(24)
bst.insert(31)
bst.insert(44)
bst.insert(66)
bst.insert(90)

bst.in_order(bst.root)
print('--------------------')
bst.pre_order(bst.root)
print('--------------------')
bst.post_order(bst.root)