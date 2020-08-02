class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.param_helper(n,n,"",res)
        return res

    def param_helper(self,leftRemain,rightRemain,path,res):
        if leftRemain<0 or rightRemain<0 or leftRemain>rightRemain:
            return
        if leftRemain==0 and rightRemain==0:
            res.append(path)
            return res
        self.param_helper(leftRemain-1,rightRemain,path+'(',res)
        self.param_helper(leftRemain,rightRemain-1,path+')',res)