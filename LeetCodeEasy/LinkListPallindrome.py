# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        node =None
        countL=0
        countS=0
        while fast and fast.next:
            node = ListNode(slow.val,node)
            fast = fast.next.next
            slow = slow.next
            countL+=2
            
        if fast:
            countL+=1
        # compare the first and second half nodes
        
        if countL%2==1 and slow.next is not None:
            slow=slow.next
        
        while node: # while node and head:
            if node.val != slow.val:
                return False
            node = node.next
            slow = slow.next
        return True
        