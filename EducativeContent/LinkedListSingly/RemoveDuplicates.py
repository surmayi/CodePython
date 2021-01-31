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

    def removeDuplicates(self):
        prev =None
        cur=self.head
        dupList=[]
        while cur:
            if cur.data in dupList:
                prev.next=cur.next
                cur=None
            else:
                dupList.append(cur.data)
                prev=cur
            cur=prev.next


llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtEnd("D")
llist.insertAtEnd("C")
llist.insertAtEnd("D")

llist.printList()

llist.insertAtEnd(('B'))

llist.removeDuplicates()
llist.printList()