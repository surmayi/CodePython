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

	def deleteNodeAtHead(self):
		if self.head is None:
			print("List is empty")
			return
		else:
			val = self.head.getData()
			self.head=self.head.getNext()
			self.decLength()
			return val

	def printList(self):
		if self.head is None:
			print("List is empty")
			return
		else:
			current = self.head
			while current!=None:
				print(current.getData(), end="->")
				current= current.getNext()
			print('None')

	def updateDataNode(self,data,updateval):
		if self.head is None:
			print("List is empty")
			return
		else:
			current = self.head
			while(current.hasNext()):
				if data == current.getData():
					current.setData(updateval)
					print("List updated with val"+str(updateval))
					return
				current=current.getNext()
			print("Data not found in List")
			return


	def insertAfterNode(self,data,node):
		if self.head is None:
			self.head=node
		else:
			current= self.head
			while(current.hasNext()):
				if(current.getData()==data):
					node.setNext(current.getNext())
					current.setNext(node)
					self.incLength()
					return
				current = current.getNext()
			current.setNext(node)
			self.incLength()
			return

	def deleteAfterNode(self,data):
		if self.head is None:
			print("List is empty")
			return
		else:
			current = self.head
			while current.hasNext():
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
			while(fast.hasNext()):
				slow=slow.getNext()
				fast = fast.getNext().getNext()
			return slow.getData()


node = Node(1)
lis = LinkedList(node)
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


lis.updateDataNode(2,10)
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


















