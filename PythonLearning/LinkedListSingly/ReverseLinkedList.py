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

    def reverseIterative(self):

        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverseRecursive(self):

        def reverseing(cur,prev):
            if not cur:
                return prev
            nxt =cur.next
            cur.next=prev
            prev=cur
            cur=nxt
            return reverseing(cur,prev)
        self.head = reverseing(self.head,None)



llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtEnd("C")
llist.insertAtEnd("D")

llist.printList()

llist.reverseIterative()
llist.printList()

llist.reverseRecursive()
llist.printList()