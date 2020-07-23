class Solution(object):
    def search(self, nums, target):
        f=0
        l=len(nums)-1
        m=0
        while f<=l:
            m=(f+l)//2
            if nums[m]<target:
                f=m+1
            elif nums[m]>target:
                l=m-1
            else:
                return m
        return -1
        