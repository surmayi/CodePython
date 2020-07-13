class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        count=0
        for i in range(0,len(nums)-1,2):
            count+= min(nums[i],nums[i+1])
        return count
        