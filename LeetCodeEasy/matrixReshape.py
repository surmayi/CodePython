class Solution(object):
    def matrixReshape(self, nums, r, c):
        import numpy as np
        nums = np.array(nums)
        if len(nums)* len(nums[0])!= r*c:
            return nums
        return nums.reshape(r,c)
    
        