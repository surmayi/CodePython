class Solution(object):
    def findRelativeRanks(self, nums):
        temp = list(nums)
        l=len(nums)
        temp.sort()
        i=l
        dic={}
        for j in temp:
            dic[j] = i
            i-=1
        for i in range(len(nums)):
            nums[i] =str(dic[nums[i]])
            if nums[i]=='1':
                nums[i]='Gold Medal'
            if nums[i]=='2':
                nums[i]= 'Silver Medal'
            if nums[i]=='3':
                nums[i]= 'Bronze Medal'
        return nums
        