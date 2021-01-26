class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,data):
        newNode= Node(data)
        if self.head is None:
            self.head=newNode
            return
        curNode=self.head
        while curNode.next:
            curNode=curNode.next
        curNode.next =newNode

    def insertAtHead(self,data):
        newNode =Node(data)
        newNode.next =self.head
        self.head=newNode
        
    def insertAfterNode(self,prevNode,data):
        if prevNode is None:
            return('Prev node is empty')
        newNode = Node(data)
        newNode.next=prevNode.next
        prevNode.next=newNode

    def insertAfterData(self,prev,data):
        if prev is None:
            return('No prev data provided')
        prevNode=self.head
        while prevNode:
            if prevNode.data==prev:
                newNode=Node(data)
                newNode.next=prevNode.next
                prevNode.next=newNode
                return
            prevNode=prevNode.next

    def printList(self):
        curNode =self.head
        while curNode:
            print(curNode.data,end='=>')
            curNode=curNode.next
        print('None')

    def deleteDataNode(self,data):
        if self.head is None:
            return('List is empty')
        if self.head.data==data:
            temp = self.head
            self.head =self.head.next
            temp.next=None
            return
        prevNode = self.head
        curNode =self.head.next
        while curNode:
            if curNode.data==data:
                prevNode.next =curNode.next
                curNode.next=None
                return
            prevNode=curNode
            curNode=curNode.next

    def deleteNodePosition(self,pos):
        if pos<0:
            return('Incorrect position provided.')
        if pos==0:
            self.deleteDataNode(self.head.data)
            return
        curNode=self.head
        count=0
        while curNode and count!=pos:
            curNode=curNode.next
            count+=1
        if curNode:
            self.deleteDataNode(curNode.data)
            return
        return('Position not found')






llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtHead("C")
llist.insertAfterData('A','E')

llist.insertAfterNode(llist.head.next, "D")

llist.printList()

llist.deleteDataNode('S')

llist.deleteNodePosition(2)
llist.printList()
