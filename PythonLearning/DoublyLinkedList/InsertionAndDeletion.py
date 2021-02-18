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

    def insertAfterDataNode(self,data,input):
        cur=self.head
        while cur:
            if cur.next is None and cur.data==data:
                self.append(input)
                return
            elif cur.data==data:
                newNode= Node(input)
                nxt = cur.next
                newNode.next=nxt
                newNode.prev=cur
                nxt.prev =newNode
                cur.next=newNode
                return
            cur=cur.next

    def insertBeforeDataNode(self,data,input):
        cur=self.head
        while cur:
            if cur.prev is None and cur.data== data:
                self.prepend(input)
                return
            elif cur.data==data:
                newNode=Node(input)
                prev=cur.prev
                newNode.next=cur
                newNode.prev=prev
                prev.next=newNode
                cur.prev=newNode
                return
            cur=cur.next

    def deleteFromList(self,data):
        cur=self.head
        while cur:
            if cur.data==data and cur==self.head:
                if cur.next is None:
                    cur=None
                    self.head=None
                    return
                else:
                    nxt =cur.next
                    nxt.prev = None
                    cur.next=None
                    cur=None
                    self.head=nxt
                    return
            elif cur.data==data:
                if cur.next is None:
                    prev= cur.prev
                    prev.next=None
                    cur.prev=None
                    cur=None
                    return
                else:
                    prev=cur.prev
                    nxt =cur.next
                    prev.next=nxt
                    nxt.prev=prev
                    cur.prev=None
                    cur.next=None
                    cur=None
                    return
            cur=cur.next


lis = DoublyLinkedList()
lis.append('A')
lis.deleteFromList('A')
lis.printList()
lis.append('B')
lis.append('C')
lis.append('D')
lis.printList()

lis.prepend('A1')
lis.prepend('B1')
lis.prepend('C1')
lis.prepend('D1')
lis.printList()

lis.insertAfterDataNode('B1','Z')
lis.printList()

lis.insertBeforeDataNode('Z','Y')
lis.printList()

lis.deleteFromList('D1')
lis.printList()

lis.deleteFromList('D')
lis.printList()

lis.deleteFromList('Z')
lis.printList()