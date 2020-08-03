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

	def deleteNode(self,val):
		if val <self.data:
			if self.left:
				self.left= self.left.deleteNode(val)
		if val>self.data:
			if self.right:
				self.right = self.right.deleteNode(val)
		else:
			if self.left is None and self.right is None:
				return None
			elif self.left is None:
				return self.right
			elif self.right is None:
				return self.left
			else:
				min = self.right.findMin()
				self.data =min
				self.right=self.right.deleteNode(min)

#				max = self.left.findMax()
#				self.data =max
#				self.left=self.left.deleteNode(max)

		return self

	def in_order_traversal(self):
		elements =[]
		if self.left:
			elements+= self.left.in_order_traversal()
		elements.append(self.data)
		if self.right:
			elements += self.right.in_order_traversal()

		return elements



elements=[17, 4, 1, 20, 9, 23, 18, 34]
root = BST(elements[0])

for i in elements[1:]:
	print('Adding Node: ',i)
	root.addNode(i)

print(root.in_order_traversal())

print('Deleting Node ', 17)
print('Deleted',root.deleteNode(17))
print(root.in_order_traversal())



