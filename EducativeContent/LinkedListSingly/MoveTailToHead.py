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

    def moveTailToHead(self):
        prev=self.head
        cur =self.head.next
        while cur.next:
            prev=cur
            cur=cur.next
        cur.next=self.head
        self.head=cur
        prev.next=None


llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtEnd("C")
llist.insertAtEnd("D")

llist.printList()

llist.moveTailToHead()
llist.printList()
