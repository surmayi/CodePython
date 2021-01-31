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

    def rotateFromNode(self,n):
        p=self.head
        q=self.head
        prev=None
        count=0
        while p and count<n:
            prev=p
            p=p.next
            q=q.next
            count+=1
        p=prev
        while q:
            prev=q
            q=q.next
        q=prev
        q.next =self.head
        self.head=p.next
        p.next = None


llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtEnd("C")
llist.insertAtEnd("D")

llist.rotateFromNode(3)
llist.printList()
