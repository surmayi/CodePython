class Solution(object):
    def findPairs(self, nums, k):
        count=0
        if k<0:
            return 0
        l =len(nums)
        s =set()
        if len(set(nums))==1 and k!=0:
            return 1
        for i in range(len(nums)):
            d=nums[i]-(k)
            if d in nums and nums.index(d)!=i and d not in s:
                count+=1
                s.add(d)
        return count