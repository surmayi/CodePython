class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        self.combine_helper(range(1,n+1),k,0,[],res)
        return res

    def combine_helper(self,n,k,index,path,res):
        if k==0:
            res.append(path)
            return
        for i in range(index,len(n)):
            self.combine_helper(n,k-1,i+1,path+[n[i]],res)