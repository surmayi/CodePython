#Iteration
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for n in nums:
            new_ans=[]
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n:
                        break
            ans =new_ans
        return ans
    
    
# Recursion

class Solution(object):
    def permuteUnique(self, nums):
        res=[]
        self.permute_helper(nums,0,[],res)
        return res

    def permute_helper(self,nums,index,path,res):
        if not nums and path not in res:
            res.append(path)
            return
        for i in range(len(nums)):
            self.permute_helper(nums[:i]+nums[i+1:],i+1,path+[nums[i]],res)
        return res
