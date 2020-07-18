class Solution(object):
    def findErrorNums(self, nums):
        nums.sort()
        val=[]
        for i in range(0,len(nums)):
            if nums[i]!=i+1:
                if nums[i]!=i+1 and (i+1) not in nums:
                    val.append(i+1)
                    break
        for i in range(0,len(nums)-1):
            if( nums[i]==nums[i+1]):
                val.insert(0,nums[i])
                return val
        