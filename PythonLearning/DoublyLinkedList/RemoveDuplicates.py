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

    def remove_duplicates(self):
        cur = self.head
        lis = []
        while cur:
            if cur.data not in lis:
                lis.append(cur.data)
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

lis = DoublyLinkedList()
lis.append('A')
lis.printList()
lis.append('B')
lis.append('C')
lis.append('D')
lis.printList()
lis.prepend('C1')

lis.prepend('A1')
lis.prepend('B1')
lis.prepend('C1')
lis.prepend('D1')
lis.prepend('D1')
lis.printList()

lis.remove_duplicates()
lis.printList()