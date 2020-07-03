class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        l=set(nums)
        a=set(i for i in range(1,len(nums)+1))
        s=list(a-l)
        return s
