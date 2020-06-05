# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        l3=None
        while((l1 is not None)and (l2 is not None)):
            print(l1.val,l2.val)
            if(l1.val<l2.val):
                l3 = ListNode(l1.val,l3)
                l1=l1.next
            else:
                l3 = ListNode(l2.val,l3)
                l2=l2.next
        while(l1 is not None):
            l3 = ListNode(l1.val,l3)
            l1=l1.next
        while(l2 is not None):
            l3 = ListNode(l2.val,l3)
            l2=l2.next
        l4=None
        while(l3 is not None):
            l4 = ListNode(l3.val,l4)
            l3 = l3.next
        return l4

head1=None
for x in [301,100,20,20,1,1]:
    head1 = ListNode(x,next =head1)
print(head1)

head2=None
for x in [305,301,201,201,100,25,10]:
    head2 = ListNode(x,next =head2)
print(head2)

m = Solution()
l3 = m.mergeTwoLists(head1,head2)
while(l3!=None):
    print(l3.val)
    l3=l3.next