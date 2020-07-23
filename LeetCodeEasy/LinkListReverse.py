# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        node =None
        while head:
            node =ListNode(head.val,node)
            head=head.next
        return node
        