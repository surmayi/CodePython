def moveZeroes( nums):
        l=len(nums)
        i=0
        while(i<l):
            if(nums[i]==0):
                nums.remove(0)
                nums.append(0)
                i-=1
                l-=1
            i+=1