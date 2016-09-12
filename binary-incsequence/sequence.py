
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self, val):
		self.root = Node(val)

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

	def longest(self, node, alltime=[], current=[]):		
		if not node:
			return

		if not len(current):
			current.append(node.val)

		if node.val > current[-1]:
			current.append(node.val)

		else:
			current = list()
			current.append(node.val)

		if len(current) > len(alltime):
			while(len(alltime)):
				alltime.pop()

			alltime.append([c for c in current])

		self.longest(node.left, alltime, current)
		self.longest(node.right, alltime, current)

		return alltime[0]

tree = Tree(10)

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
