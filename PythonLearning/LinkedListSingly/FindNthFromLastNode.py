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

    def findNthFromLastNode(self,n,method):
        if method==1:
            len = self.getLength(self.head) -1
            cur = self.head
            while cur:
                if n==len:
                    return cur.data
                len-=1
                cur=cur.next
            if not cur:
                return 'Node not found'
        else:
            p=self.head
            q=self.head
            while q.next and n>0:
                q=q.next
                n-=1
            if not q:
                return 'Node not found'
            while p and q.next:
                p=p.next
                q=q.next
            return p.data

llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtEnd("C")
llist.insertAtEnd("D")

print(llist.getLength(llist.head))
llist.printList()
print(llist.findNthFromLastNode(5,1))
print(llist.findNthFromLastNode(2,2))