class Solution(object):
    def subsetsWithDup(self, nums):
        res=[]
        nums.sort()
        self.set_helper(nums,0,[],res)
        return res
    
    def set_helper(self,nums,index,path,res):
        if path not in res:
            res.append(path)
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            self.set_helper(nums,i+1,path+ [nums[i]],res)
        return res
        
