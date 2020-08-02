class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()
        self.combine_helper(candidates,target,[],res)
        return res

    def combine_helper(self,candidates,target, path,res):
        if target ==0:
            if path not in res:
                res.append(path)
            return
        for i in range(0,len(candidates)):
            if target-candidates[i] <0:
                break
            self.combine_helper(candidates[i+1:],target-candidates[i], path+[candidates[i]],res)