# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans =[]
        self.helper(root,0,ans)
        return [s/c for s,c in ans]
    
    def helper(self,node,level,ans):
        if node:
            if len(ans)<=level:
                ans.append([0,0])
            ans[level][0] +=node.val
            ans[level][1] +=1
            self.helper(node.left,level+1,ans)
            self.helper(node.right,level+1,ans)
        return ans