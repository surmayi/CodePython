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

    def swapNodes(self,data1,data2):
        if data1==data2:
            return('Both are same nodes')
        prev1,prev2=None,None
        cur1,cur2=self.head,self.head
        # record the prev node and current node for data1
        while cur1 and cur1.data!=data1:
            prev1=cur1
            cur1=cur1.next
        # record the prev node and current node for data2
        while cur2 and cur2.data!=data2:
            prev2=cur2
            cur2=cur2.next
        # set next of prev1 node to cur2 node, set cur2 as head if no prev, meaning cur1 was the head node.
        if prev1:
            prev1.next=cur2
        else:
            self.head=cur2

        if prev2:
            prev2.next=cur1
        else:
            self.head=cur1
        # interchange next of cur1 and cur2
        cur1.next,cur2.next =cur2.next,cur1.next


llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtEnd("C")
llist.insertAtEnd("D")

llist.printList()

llist.swapNodes('B','A')

llist.printList()