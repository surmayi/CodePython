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


    def mergeSortedLists(self,l2):
        if self.head is None:
            return l2
        if l2.head is None:
            return self.head
        p=self.head
        q=l2.head
        s=None
        if p.data<=q.data:
            s=p
            p=s.next
        else:
            s=q
            q=s.next
        new_head = s

        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next

        if p:
            s.next=p
        if q:
            s.next=q
        return new_head





list1 = LinkedList()
list1.insertAtEnd(1)
list1.insertAtEnd(5)
list1.insertAtEnd(6)
list1.insertAtEnd(8)

list1.printList()

list2 = LinkedList()
list2.insertAtEnd(2)
list2.insertAtEnd(3)
list2.insertAtEnd(4)
list2.insertAtEnd(7)

list2.printList()

list3 = LinkedList()
list3.head= list1.mergeSortedLists(list2)
list3.printList()