class Solution(object):
    def combinationSum(self, candidates, target):
        res =[]
        candidates.sort()
        self.combine_helper(candidates,target,0,[],res)
        return res

    def combine_helper(self,nums,target,index,path,res):
        if target==0:
            res.append(path)
            return
        for i in range(index,len(nums)):
            if target-nums[i]<0:
                break
            self.combine_helper(nums,target-nums[i],i,path+[nums[i]],res)
        return res
        
