class Solution(object):
    def findDuplicates(self, nums):
        res=[]
        for i in range(0,len(nums)):
            if nums[abs(nums[i])-1]<0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1]*=-1
        return res