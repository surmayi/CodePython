# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter =[0]
        self.helper(root,diameter)
        return diameter[0]

    def helper(self,node,diameter):
        if not node:
            return 0
        left = self.helper(node.left,diameter)
        right = self.helper(node.right,diameter)
        diameter[0] = max(diameter[0],left+right)
        return 1+ max(left,right)