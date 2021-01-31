class Node:
    def __init__(self, data):
        self.data=data
        self.next =None


class CircularLinkedlist:

    def __init__(self):
        self.head=None

    def appendAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head =newNode
            self.head.next=self.head
        else:
            cur =self.head
            while cur:
                if cur.next==self.head:
                    cur.next=newNode
                cur=cur.next
            newNode.next=self.head

    def prependAtHead(self,data):
        newNode =Node(data)
        newNode.next=self.head
        if not self.head:
            newNode.next=newNode
        else:
            cur = self.head
            while cur.next!=self.head:
                cur=cur.next
            cur.next=newNode
        self.head=newNode

    def remove(self,data):
        if not self.head:
            return 'Empty list'
        cur = self.head
        if data==self.head.data:
            while cur.next!=self.head:
                cur=cur.next
            cur.next=self.head.next
            self.head= self.head.next
        else:
            prev=None
            while cur.data!=data:
                prev =cur
                cur=cur.next
                if cur.next==self.head:
                    return 'Node not found'
            prev.next =cur.next

    def removeNode(self,node):
        if not self.head or not node:
            return 'Nothing to do'
        cur =self.head
        if node==self.head:
            while cur.next!=self.head:
                cur=cur.next
            if self.head==self.head.next:
                self.head=None
            else:
                cur.next=self.head.next
                self.head=self.head.next
        else:
            prev=None
            while cur.next!=self.head:
                prev=cur
                cur=cur.next
                if cur==node:
                    prev.next =cur.next
                    cur=cur.next

    def __len__(self):
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
            if cur==self.head:
                break
        return count

    def josephusCircle(self,k):
        cur =self.head
        print(len(self))
        while len(self)>1:
            count=1
            while count!=k:
                cur =cur.next
                count+=1
            print('Removing: '+cur.data)
            self.removeNode(cur)
            self.printList()
            cur=cur.next


    def printList(self):
        cur =self.head
        while cur:
            print(cur.data,end='->')
            if cur.next==self.head:
                break
            cur = cur.next
        print('None')


lis = CircularLinkedlist()
lis.appendAtEnd('A')
lis.appendAtEnd('B')
lis.appendAtEnd('C')
lis.appendAtEnd('D')
lis.remove('A')
lis.printList()

lis.prependAtHead('A1')
lis.prependAtHead('B1')
lis.appendAtEnd('C')
lis.appendAtEnd('D')
lis.prependAtHead('C1')
lis.prependAtHead('D1')

lis.printList()
lis.josephusCircle(2)