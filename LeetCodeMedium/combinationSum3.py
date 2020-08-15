class Solution(object):
    def combinationSum3(self, k, n):
        nums = range(1,10)
        res=[]
        self.combine_helper(nums,k,n,[],res)
        return res
    def combine_helper(self,nums,length,target,path,res):
        if length==0 and target==0:
            res.append(path)
            return
        for i in range(len(nums)):
            if target-nums[i] <0 or length <0:
                break
            self.combine_helper(nums[i+1:],length-1,target-nums[i],path+[nums[i]],res)
        
