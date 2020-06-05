def twoSum( nums, target):
        for i,num in enumerate(nums):
            temp = target - num
            if (temp in nums):
                ind = nums.index(temp)
                if ind != i:
                    return [i,ind]

twoSum([2, 7, 11, 15],9)