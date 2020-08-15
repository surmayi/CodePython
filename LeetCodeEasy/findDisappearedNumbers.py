class Solution(object):
    def findDisappearedNumbers(self, nums):
        s=set(nums)
        temp =[]
        for i in range(1,len(nums)+1):
            if i not in s:
                temp.append(i)
        return temp
        
