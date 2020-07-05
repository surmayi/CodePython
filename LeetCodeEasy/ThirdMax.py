class Solution(object):
    def thirdMax(self, nums):
        l=len(nums)
        i=0
        if(len(set(nums))<3):
             return max(nums)
        while(l>0 and i<3):
            m= max(nums)
            while(m in nums):
                nums.remove(max(nums))
            l-+1
            i+=1
        return m