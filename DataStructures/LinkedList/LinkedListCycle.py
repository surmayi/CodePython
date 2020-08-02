class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

	def setData(self,data):
		self.data=data

	def getData(self):
		return self.data

	def setNext(self,next):
		self.next=next

	def getNext(self):
		return self.next

	def hasNext(self):
		return self.next!=None

	def __print__(self):
		print('This is', self.data)


class LinkedList:
	def __init__(self,node):
		self.head=node
		self.len=1

	def incLength(self):
		self.len+=1

	def decLength(self):
		self.len-=1

	def getLength(self):
		return self.len

	def getHead(self):
		return self.head

	def insertNodeAtHead(self,node):
		if self.head is None:
			self.head=node
		else:
			node.setNext(self.head)
			self.head = node
		self.incLength()

	def checkLoopInList(self):
		if self.head is None:
			print('List is empty')
			return
		else:
			slow = self.head
			fast = self.head.getNext()
			while(slow!=fast):
				slow=slow.getNext()
				if fast!=None:
					fast = fast.getNext().getNext()
				else:
					return False
			return True

