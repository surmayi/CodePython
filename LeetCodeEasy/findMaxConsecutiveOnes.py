class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if len(nums)==0:
            return 0
        count=0
        i=0
        l=len(nums)
        n=[]
        while(i<l):
            if nums[i]==1:
                count+=1
            else:
                n.append(count)
                count=0
            i+=1
        n.append(count)
        return max(n)
        