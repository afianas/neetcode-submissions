# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.diameter=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.BinaryTree(root)
        return self.diameter
    def BinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left=self.BinaryTree(root.left)
        right=self.BinaryTree(root.right)
        self.diameter=max(self.diameter,left+right)
        return 1+max(left,right)