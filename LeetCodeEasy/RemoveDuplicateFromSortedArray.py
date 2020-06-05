def removeDuplicates(self, nums):
        if len(nums) in [0,1]:
            return len(nums)
        i=0
        while(i<len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums.pop(i)
            else:
                i+=1
        return len(nums)

removeDuplicates([0,0,1,1,1,2,2,3,3,4])