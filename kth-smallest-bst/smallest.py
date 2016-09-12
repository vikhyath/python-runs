class Node:
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None
		self.count = 0


class BST:
	def __init__(self):
		self.root = None
		self.stack = []
		self.stacktip = None
		pass

	def insert(self, val):
		node = Node(val)
		self._find_and_insert(node, self.root)

	def _find_and_insert(self, node, head):
		if not self.root:
			self.root = node
			return

		if node.val < head.val:
			head.count += 1
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

	def inorder(self, head):
		if not head:
			return
		self.inorder(head.left)
		print(str(head.val) + ' (' + str(head.count) + ') ')
		self.inorder(head.right)

	def smallest(self, head, kth):
		if kth == head.count + 1:
			return head.val

		if kth > head.count + 1:
			return self.smallest(head.right, kth - head.count - 1)
		else:
			return self.smallest(head.left, kth)


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

bst.inorder(bst.root)

print(bst.smallest(bst.root, 1))
print(bst.smallest(bst.root, 2))
print(bst.smallest(bst.root, 3))
print(bst.smallest(bst.root, 4))
print(bst.smallest(bst.root, 5))
print(bst.smallest(bst.root, 6))
print(bst.smallest(bst.root, 7))
print(bst.smallest(bst.root, 8))
print(bst.smallest(bst.root, 9))
print(bst.smallest(bst.root, 10))
print(bst.smallest(bst.root, 11))
print(bst.smallest(bst.root, 12))
print(bst.smallest(bst.root, 13))
print(bst.smallest(bst.root, 14))
print(bst.smallest(bst.root, 15))
