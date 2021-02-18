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


    def pairsWithSums(self,data):
        p=None
        q=self.head
        lis=[]
        while q:
            p=q.next
            while p:
                if p.data+q.data==data:
                    lis.append((q.data,p.data))
                p=p.next
            q=q.next
        return lis


lis = DoublyLinkedList()
lis.append(1)
lis.append(2)
lis.append(4)
lis.append(3)
lis.printList()

print(lis.pairsWithSums(5))