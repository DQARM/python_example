class Tree(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.left.left = Tree()
root.left.left.data = "left_left"
root.right = Tree()
root.right.data = "right"
root.right.right = Tree()
root.right.data="right_right"

print root
print root.data
print root.left
print root.left.data
print root.right
print root.right.data
print root.left.left
print root.left.left.data
