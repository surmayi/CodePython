def majorityElement( nums):
        setnum= set(nums)
        check = len(nums)//2
        for i in setnum:
            c=0
            while(i in nums):
                nums.remove(i)
                c+=1
                if(c>check):
                    return i
majorityElement([2,2,1,1,1,2,2])