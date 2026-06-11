# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.i=0
        self.r=TreeNode
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxVal):
            if not root:
                return 0
            res=0
            if root.val>=maxVal:
                maxVal=max(root.val,maxVal)
                res=1
            res+=dfs(root.left,maxVal)
            res+=dfs(root.right,maxVal)

            return res
        return dfs(root,float("-inf"))

