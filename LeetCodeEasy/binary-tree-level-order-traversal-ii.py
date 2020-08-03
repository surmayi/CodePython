# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans =[]
        self.helper(root,0,ans)
        return ans[::-1]
    
    def helper(self,node,level,ans):
        if node:
            if len(ans)<=level:
                ans.append([])
            ans[level].append(node.val)
            self.helper(node.left,level+1,ans)
            self.helper(node.right,level+1,ans)
        return ans