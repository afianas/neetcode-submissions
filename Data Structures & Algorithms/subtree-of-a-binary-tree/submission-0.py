# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and subRoot:
            return False
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return False
        if self.isSameTree(root,subRoot):
            return True
        else:
            left=self.isSubtree(root.left,subRoot)
            right=self.isSubtree(root.right,subRoot)

        if left:
            return True
        elif right:
            return True
        else:
            return False
    def isSameTree(self,root:  Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return False
        if root.val!=subRoot.val:
            return False

        left=self.isSameTree(root.left,subRoot.left)
        right=self.isSameTree(root.right,subRoot.right)

        return left and right