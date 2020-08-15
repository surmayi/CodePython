# Iteration
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            for i in result:
                result = result + [i + [num] ]
        return result
 
# Recursion
class Solution(object):
    def subsets(self, nums):
        res =[]
        self.set_helper(nums,0,[],res)
        return res

    def set_helper(self,nums,index,path,res):
        res.append(path)
        for i in range(index,len(nums)):
            self.set_helper(nums,i+1,path+[nums[i]],res)
        return res
        
