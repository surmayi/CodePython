def removeElement( nums, val):
        while(val in nums):
            nums.remove(val)
            print(nums)
        return len(nums)

removeElement([3,2,2,3],3)
removeElement([0,1,2,2,3,0,4,2],2)