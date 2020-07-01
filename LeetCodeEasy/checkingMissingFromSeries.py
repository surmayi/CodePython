class Solution(object):
    def missingNumber(self, nums):
        n= len(nums)
        sum1 = n*(n+1)/2
        for i in nums:
            sum1=sum1-i
        return sum1