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

    def printList(self):
        curNode =self.head
        while curNode:
            print(curNode.data,end='=>')
            curNode=curNode.next
        print('None')

    def getLength(self,node):
        if node is None:
            return 0
        return 1+ self.getLength(node.next)


llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtEnd("C")
llist.insertAtEnd("D")

print(llist.getLength(llist.head))
llist.printList()