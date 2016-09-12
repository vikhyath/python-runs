# Given preorder traversal of a binary search tree, construct the BST.

# For example, if the given traversal is {10, 5, 1, 7, 40, 50}, 
# then the output should be root of following tree.

#      10
#    /   \
#   5     40
#  /  \      \
# 1    7      50  

#!/usr/bin/env python

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self, root):
		self.root = None

	def tree(self, node=None):
		if node and (node.left or node.right):
			print(str(node.val) + ' -> ', end='')
			if node.left:
	
				print(' L ' + str(node.left.val), end='')

			if node.right:
				print(' R ' + str(node.right.val))
			self.tree(node.left)
			self.tree(node.right)

	def reconstruct(self, ino, pre):
		pstart = 0
		pend = len(pre) - 1
		istart = 0
		iend = len(ino) - 1

		self.__reconstruct(ino, pre, pstart, pend, istart, iend)

	def __reconstruct(self, ino, pre, pstart, pend, istart, iend):
		if pstart > pend or istart > iend:
			return None

		val = pre[pstart]
		node = Node(val)

		if not self.root:
			self.root = node

		idx = istart
		while idx <= iend:
			if ino[idx] == val:
				break

			idx += 1

		node.left = self.__reconstruct(ino, pre, pstart + 1, pstart+(idx-istart), istart, idx-1)
		node.right = self.__reconstruct(ino, pre, pstart+(idx-istart)+1, pend, idx+1, iend)

		return node

tree = Tree(None)
tree.reconstruct(ino=[4, 2, 5, 1, 6, 7, 3, 8], pre=[1, 2, 4, 5, 3, 7, 6, 8])
tree.tree(tree.root)

