# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        else:
            val1 = 1 + self.maxDepth(root.right)
            val2 = 1 + self.maxDepth(root.left)
            return max(val1, val2)
        