class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        candidates=range(1,10)
        self.combine_helper(candidates,k, n,[],res)
        return res

    def combine_helper(self,candidates,length, target,path,res):
        if length==0 and target==0:
            if path not in res:
                res.append(path)
                return
        for i in range(len(candidates)):
            if target-candidates[i]<0 or length<0:
                break
            self.combine_helper(candidates[i+1:],length-1,target-candidates[i],path+[candidates[i]],res)
