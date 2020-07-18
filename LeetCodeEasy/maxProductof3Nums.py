class Solution(object):
    def maximumProduct(self, nums):
        if len(nums)<3:
            return 0
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        nums.sort(reverse=True)
        if(nums[0]<0):
            return nums[0]*nums[1]*nums[2]
        else:
            if nums[-1]<0 and nums[-2] and nums[-1]*nums[-2]> nums[1]*nums[2]:
                    return nums[0]*nums[-1]*nums[-2] 
        return nums[0]*nums[1]*nums[2]
        