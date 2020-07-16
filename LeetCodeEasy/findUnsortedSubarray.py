class Solution(object):
    def findUnsortedSubarray(self, nums):
        if nums[0]> nums[-1]:
            return len(nums)
        if len(nums) in[0,1]:
            return 0
        l=len(nums)
        frontind =0
        backind =l-1
        i=0
        frontdone =False
        backdone = False
        while(i<l-1):
            if(frontdone is False and nums[i]<=nums[i+1]):
                frontind+=1
            else:
                frontdone=True
            if(backdone is False and nums[l-i-1]>=nums[l-i-2]):
                backind-=1
            else:
                backdone =True
            i+=1
        if frontind>=backind:
            return 0
        temp = nums[frontind:backind+1]
        tmin = min(temp)
        tmax = max(temp)
        while frontind>0 and nums[frontind-1]>tmin:
            frontind-=1
        while backind<l-1 and nums[backind+1]<tmax:
            print(backind)
            backind+=1
        return backind-frontind+1
        