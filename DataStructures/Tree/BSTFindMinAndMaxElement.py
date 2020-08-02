class BST:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

	def addNode(self,data):
		if data ==self.data:
			return
		if data< self.data:
			if self.left:
				self.left.addNode(data)
			else:
				self.left= BST(data)
				return
		else:
			if self.right:
				self.right.addNode(data)
			else:
				self.right= BST(data)
				return

	def findMin(self):
		print(self.data)
		if self.left:
			return self.left.findMin()
		else:
			return self.data

	def findMax(self):
		print(self.data)
		if self.right:
			return self.right.findMax()
		else:
			return self.data


elements=[17, 4, 1, 20, 9, 23, 18, 34]
root = BST(elements[0])

for i in elements[1:]:
	print('Adding Node: ',i)
	root.addNode(i)

print('Min element: ',root.findMin())

print('Max Element: ',root.findMax())

