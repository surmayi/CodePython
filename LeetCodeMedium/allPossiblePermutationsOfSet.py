class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        return self.permute_helper(nums,[],res)


    def permute_helper(self,nums,path,res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.permute_helper(nums[:i]+nums[i+1:],path+[nums[i]],res)
        return res