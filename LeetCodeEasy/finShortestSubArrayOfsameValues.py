class Solution(object):
    def findShortestSubArray(self, nums):
        d={}
        r =0
        keys=[]
        for i in range(0,len(nums)):
            if nums[i] in d.keys():
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        newd={}
        for key,val in d.items():
            newd[key] = [len(val),max(d[key])-min(d[key])]
        mi =max(newd.values())
        for val in newd.values():
            if val[0] == mi[0] and val[1]<mi[1]:
                mi = val
        return mi[1]+1
        