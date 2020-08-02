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


class CircularLinkedList:
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
		node.setNext(node)
		if self.head is None:
			self.head=node
		else:
			node.setNext(self.head)
			current= self.head
			while(current.getNext()!=self.head):
				current=current.getNext()
			current.setNext(node)
			self.head = node
		self.incLength()

	def deleteNodeAtHead(self):
		if self.head is None:
			print("List is empty")
			return
		else:
			if self.head.getNext()==None:
				self.head=None
				return
			else:
				current=self.head.getNext()
				while current!=None and current.getNext()!=self.head:
					current=current.getNext()
				current.setNext(self.head.getNext())
				self.head=self.head.getNext()
				self.decLength()
				return


	def printList(self):
		if self.head is None:
			print("List is empty")
			return
		else:
			print(self.head.getData(), end="->")
			current = self.head.getNext()
			while current!=None and current!=self.head:
				print(current.getData(), end="->")
				current= current.getNext()
			print('None')


	def insertAfterNode(self,data,node):
		node.setNext(node)
		if self.head is None:
			self.head=node
			return
		else:
			current= self.head
			while(current.getNext()!=self.head):
				if(current.getData()==data):
					node.setNext(current.getNext())
					current.setNext(node)
					self.incLength()
					return
				current = current.getNext()
			current.setNext(node)
			node.setNext(self.head)
			self.incLength()
			return


	def deleteNode(self,data):
		if self.head is None:
			print("List is empty")
			return
		else:
			if self.head.getData==data:
				self.head=None
				return
			else:
				current = self.head.getNext()
				prev = self.head
				while current.getNext()!=self.head:
					if(current.getData() == data):
						prev.setNext(current.getNext().getNext())
						self.decLength()
						return
					prev=current
					current = current.getNext()
				if(current.getData() == data):
					prev.setNext(self.head)
					self.decLength()
			return "Data Not found in List"


	def deleteAfterNode(self,data):
		if self.head is None:
			print("List is empty")
			return
		else:
			current = self.head.getNext()
			prev = self.head
			if prev.getData()==data:
				self.head.setNext(None)
				self.decLength()
				return
			else:
				while current.getNext()!=self.head:
					if(current.getData() == data):
						current.setNext(current.getNext().getNext())
						self.decLength()
						return
					current = current.getNext()
			return "Data Not found in List"


	def findMiddleElement(self):
		if self.head is None:
			print('List is empty')
			return
		else:
			slow = self.head
			fast = self.head
			while(fast.getNext()!=self.head):
				slow=slow.getNext()
				fast = fast.getNext().getNext()
			return slow.getData()


node = Node(1)
lis = CircularLinkedList(node)
lis.printList()

lis.deleteNodeAtHead()
lis.printList()
lis.deleteAfterNode(1)
lis.printList()

lis.insertNodeAtHead(Node(1))
lis.insertNodeAtHead(Node(2))
lis.insertNodeAtHead(Node(3))
lis.insertNodeAtHead(Node(4))
lis.printList()


lis.deleteNodeAtHead()
lis.printList()
lis.insertNodeAtHead(Node(4))
lis.deleteAfterNode(3)
lis.printList()
lis.insertAfterNode(4,Node(8))
lis.insertNodeAtHead(Node(5))
lis.printList()
e = lis.findMiddleElement()
print(e)

