# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
			return
        else:
            slow = head
            fast = head.next
            while(slow!=fast):
                slow=slow.next
                if fast and fast.next:
                    fast = fast.next.next
                else:
                    return False
            return True
        