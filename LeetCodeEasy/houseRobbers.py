class Solution(object):
    def rob(self, nums):
        prev=0
        cur=0
        for i in nums:
            temp = prev
            prev =cur
            cur = max(temp+i ,cur)
        return cur
            
        