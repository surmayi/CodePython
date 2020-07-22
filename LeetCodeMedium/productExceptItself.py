class Solution(object):
    def productExceptSelf(self, nums):
        l=len(nums)
        output = [1]* l
        f=b=1
        for i in range(l):
            output[i]*=f
            output[-1-i]*=b
            f*=nums[i]
            b*=nums[-1-i]
        return output
        