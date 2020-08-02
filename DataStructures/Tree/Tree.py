class Tree:
	def __init__(self,data):
		self.parent=None
		self.data=data
		self.children=[]

	def addChild(self,child):
		child.parent= self
		self.children.append(child)

	def printTree(self, type=None):
		prefix = self.getLevel() * '  ' + '|__'  if self.parent else ''
		if type in [None,'both']:
			print(prefix+ self.data)
		if type =='names':
			print(prefix+ self.data.split(' ')[0])
		if type == 'designations':
			print(prefix+ ' '.join(self.data.split(' ')[1:]))
		if self.children:
			for child in self.children:
				child.printTree(type)

	def getLevel(self):
		level=0
		p=self.parent
		while p:
			level+=1
			p=p.parent
		return level



ceo = Tree('Nilupul CEO')

cto= Tree('Chinmay CTO')
hr = Tree('Gels HR Head')

infra= Tree('Vishwa Infra Head')
infra.addChild(Tree('Dhawal Cloud Manager'))
infra.addChild(Tree('Abhijeet App Manager'))
cto.addChild(infra)

hr.addChild(Tree('Peter Recruitment Manager'))
hr.addChild(Tree('Waqas Policy Manager'))

ceo.addChild(cto)
ceo.addChild(hr)

ceo.printTree()
ceo.printTree('both')
ceo.printTree('names')
ceo.printTree('designations')








