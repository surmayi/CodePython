class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,data):
        newNode =Node(data)
        newNode.next =self.head
        self.head=newNode

    def printList(self):
        curNode =self.head
        while curNode:
            print(curNode.data,end='=>')
            curNode=curNode.next
        print('None')


    def addLists(self,lis2):
        list1=[]
        list2=[]
        cur1=self.head
        while cur1:
            list1.append(cur1.data)
            cur1=cur1.next
        cur2 =lis2
        while cur2:
            list2.append(cur2.data)
            cur2=cur2.next
        s1=0
        s2=0
        while len(list1)>0:
            s1=s1*10+list1.pop()
        while len(list2)>0:
            s2=s2*10+list2.pop()
        s3=list(str(s1+s2))
        lis3 =LinkedList()
        for i in s3:
            lis3.insertAtEnd(i)
        return lis3


llist1 = LinkedList()
llist1.insertAtEnd(3)
llist1.insertAtEnd(6)
llist1.insertAtEnd(5)
llist1.printList()
llist2 = LinkedList()
llist2.insertAtEnd(2)
llist2.insertAtEnd(4)
#llist2.insertAtEnd(8)
llist2.printList()
llist3=llist1.addLists(llist2.head)
llist3.printList()
