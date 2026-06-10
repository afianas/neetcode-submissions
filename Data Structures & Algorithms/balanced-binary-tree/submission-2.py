# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.val = True

    def isBalanced(self, root) -> bool:
        self.height(root)

        if not self.val:
            return False
        else:
            return True

    def height(self, root) -> int:
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            self.val = False

        return 1 + max(left, right)