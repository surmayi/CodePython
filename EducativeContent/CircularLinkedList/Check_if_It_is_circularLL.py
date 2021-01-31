from EducativeContent.LinkedListSingly.InsertionAndDeletion import LinkedList

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

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur:
            if cur.next == input_list.head:
                return True
            elif cur.next == None:
                return False
            else:
                cur = cur.next

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

lis.printList()

lis.prependAtHead('A1')
lis.prependAtHead('B1')
lis.appendAtEnd('C')
lis.appendAtEnd('D')
lis.prependAtHead('C1')
lis.prependAtHead('D1')

lis.printList()
print(lis.is_circular_linked_list(lis))

llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtHead("C")
llist.insertAfterData('A','E')

llist.insertAfterNode(llist.head.next, "D")

llist.printList()

print(lis.is_circular_linked_list(llist))