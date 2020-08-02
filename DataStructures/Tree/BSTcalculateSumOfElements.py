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

	def calculateSum(self):
		sum=self.data
		if self.left:
			sum+=self.left.calculateSum()

		if self.right:
			sum+=self.right.calculateSum()
		return sum

elements=[17, 4, 1, 20, 9, 23, 18, 34]
print(sum(elements))
root = BST(elements[0])

for i in elements[1:]:
	print('Adding Node: ',i)
	root.addNode(i)

print(root.calculateSum())

