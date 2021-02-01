class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next =None


class DoublyLinkedList:

    def __init__(self):
        self.head =None

    def append(self,data):
        newNode = Node(data)
        if not self.head:
            self.head=newNode
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=newNode
            newNode.prev=cur

    def prepend(self,data):
        newNode = Node(data)
        if not self.head:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

    def printList(self):
        cur=self.head
        while cur:
            print(cur.data,end='->')
            cur =cur.next
        print('None')

    def reverseList(self):
        temp =None
        cur=self.head
        while cur:
            temp =cur.prev
            cur.prev=cur.next
            cur.next=temp
            cur=cur.prev
        if temp:
            self.head=temp.prev


lis = DoublyLinkedList()
lis.append('A')
lis.append('B')
lis.append('C')
lis.append('D')
lis.printList()

lis.reverseList()
lis.printList()