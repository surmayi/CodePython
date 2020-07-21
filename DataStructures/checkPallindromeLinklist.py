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
	def __init__(self,node=None):
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

	def checkPallindrome(self):
		ele, newlist = self.findMiddleNode()
		print(ele.getData())
		newlist.printList()
		print(ele.getNext().getData())
		if self.len%2==0:
			print('Here',self.len)
			ele=ele.getNext()
		while ele!=None:
			print(newlist.head.getData(),ele.getData() )
			if ele.getData()==newlist.head.getData():
				ele=ele.getNext()
				newlist.head= newlist.head.getNext()
			else:
				print('False')
				return False
		print('True')
		return True

	def findMiddleNode(self):
		if self.head is None:
			print('List is empty')
			return
		else:
			slow = self.head
			fast = self.head
			new = LinkedList()
			while(fast is not None and fast.hasNext()):
				new.insertNodeAtHead(Node(slow.getData()))
				slow=slow.getNext()
				fast = fast.getNext().getNext()
			return slow,new

node1 = Node(3)

lis1 =LinkedList()
lis1.insertNodeAtHead(Node(2))
lis1.insertNodeAtHead(Node(4))
lis1.insertNodeAtHead(Node(3))
lis1.insertNodeAtHead(Node(5))
lis1.insertNodeAtHead(Node(3))
lis1.insertNodeAtHead(Node(4))
lis1.insertNodeAtHead(Node(2))
lis1.printList()
x,y = lis1.findMiddleNode()

lis1.checkPallindrome()

