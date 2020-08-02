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

	def __init__(self):
		self.head =None
		self.len=0

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

	def changeToVal(self):
		if self.head is None:
			return 0
		val =0
		current = self.head
		while(current!=None):
			val= val*10+ current.getData()
			current=current.getNext()
		return val

def addTwoNumbers( l1, l2):
    track = cur = Node(0)
    carry = 0
    while l1.head is not None or l2.head is not None or carry!=0:
        if l1:
            carry += l1.getHead().getData()
            l1.head = l1.getHead().getNext()
        if l2:
            carry += l2.getHead().getData()
            l2.head = l2.getHead().getNext()
        cur = Node(carry%10)
        cur = cur.getNext()
        carry //= 10
    return track


node1 = Node(3)

lis1 =LinkedList()
lis1.insertNodeAtHead(Node(2))
lis1.insertNodeAtHead(Node(4))
lis1.insertNodeAtHead(Node(3))
lis1.printList()
print(lis1.changeToVal())

node2 = Node(4)

lis2 =LinkedList()
lis2.insertNodeAtHead(Node(5))
lis2.insertNodeAtHead(Node(6))
lis2.insertNodeAtHead(Node(4))
lis2.printList()
print(lis2.changeToVal())

num = str(lis1.changeToVal()+lis2.changeToVal())
num=list(num)
lis3= LinkedList()
for i in num:
	lis3.insertNodeAtHead(Node(int(i)))
lis3.printList()

n= addTwoNumbers(lis1,lis2)
while(n is not None):
	print(n.data)
	n = n.getNext()
	






