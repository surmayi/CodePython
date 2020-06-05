class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates( head):
        if(head is None):
            return None
        new = None
        while(head.next!=None):
            if(head.val==head.next.val):
                head=head.next
            else:
                new = ListNode(head.val,new)
                head= head.next
        new = ListNode(head.val,new)
        l4=None
        while(new is not None):
            l4 = ListNode(new.val,l4)
            new = new.next
        return l4



head1=None
for x in [5,3,2,1]:
    head1 = ListNode(x,next =head1)
l4 = deleteDuplicates(head1)

while(l4!=None):
    print(l4.val)
    l4=l4.next