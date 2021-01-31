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

    def checkIfPallindrome(self,method):
        if method==1:
            cur =self.head
            s=''
            while cur:
                s+=cur.data
                cur=cur.next
            return s[:]==s[::-1]
        elif method==2:
            cur=self.head
            lis=[]
            while cur:
                lis.append(cur.data)
                cur=cur.next
            cur=self.head
            while cur:
                if cur.data!=lis.pop():
                    return False
                cur=cur.next
            return True
        else:
            p=self.head
            q=self.head
            prev=[]
            count=0
            while q:
                prev.append(q)
                count+=1
                q=q.next
            q=prev[count-1]

            i=1
            while i<= count//2+1:
                if prev[-i].data!=p.data:
                    return False
                i+=1
                p=p.next
            return True

llist = LinkedList()
llist.insertAtEnd("A")
llist.insertAtEnd("B")
llist.insertAtEnd("C")
llist.insertAtEnd("B")
llist.insertAtEnd("A")

llist.printList()

print(llist.checkIfPallindrome(1))
print(llist.checkIfPallindrome(2))
print(llist.checkIfPallindrome(3))