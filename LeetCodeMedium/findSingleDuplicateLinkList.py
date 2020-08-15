class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        #first find the index from where to start searching, slow jumps 1 step, fast jumps 2 steps, until they meet, ie both have same value
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
        # index found at fast, now start slow from begining and fast from the index found in above loop
        slow = nums[0];
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
        
