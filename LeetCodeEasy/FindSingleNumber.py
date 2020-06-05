def singleNumber( nums):
        l=len(nums)
        while(l>0):
            t= nums.pop()
            if t in nums:
                h = nums.remove(t)
                l-=1
            else:
                return t
            l-=1

singleNumber([2,2,1])
singleNumber([4,1,2,1,2])