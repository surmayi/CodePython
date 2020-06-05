def searchInsert( nums, target):
        if target in nums:
            return nums.index(target)
        else:
            if(target<nums[0]):
                return 0
            for i in range(0,len(nums)):
                if(nums[i]>target):
                    return i
            return len(nums)

searchInsert([1,3,5,6], 5)
searchInsert([1,3,5,6], 7)