# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if (not root):
            return res
        
        else:
            res = max(res, self.maxDepth(root.left) + self.maxDepth(root.right))
            res = max(res, self.diameterOfBinaryTree(root.left))
            res = max(self.diameterOfBinaryTree(root.right), res)
        return res
        

    def maxDepth(self, root):
        if (not root):
            return 0
        else:
            v1 = 1 + self.maxDepth(root.left)
            v2 = 1 + self.maxDepth(root.right)
            return max(v1, v2)
        