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

    def countOccurance(self,data,method,cur=None):
        if method==1:
            cur=self.head
            count=0
            while cur:
                if data==cur.data:
                    count+=1
                cur=cur.next
            return count
        else:
            if not cur:
                return 0
            if data==cur.data:
                return 1+ self.countOccurance(data,2,cur.next)
            else:
                return self.countOccurance(data,2,cur.next)


llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtEnd("C")
llist.insertAtEnd("B")
llist.insertAtEnd("B")
llist.insertAtEnd("D")

llist.printList()
print(llist.countOccurance('B',1))
print(llist.countOccurance('B',2,llist.head))