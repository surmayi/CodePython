# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while head and head.val==val:
            head=head.next
        if head is None:
            return None
        temp =head
        while temp and temp.next:
            if temp.next.val==val:
                temp.next = temp.next.next
            else:
                temp=temp.next
        return head
    