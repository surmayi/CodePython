class Solution(object):
    def findLHS(self, nums):
        done={}
        for i in nums:
            if i in done:
                done[i]+=1
            else:
                done[i]=1
        mx=0
        for key in done:
            if done.get(key+1):
                mx = max(mx,done[key]+ done[key+1] )
        return mx