# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #as it is a BST, we know the L<M<R, so we can compare P and Q to
        #differentiate between vals, against root.... if the root is greater than
        #both then we make root left, and if less than both then we go right
        # if one is equal/less and one is greater or other than 
        #we know this is the LCA.
        if (not p or not q or not root):
            return None
        elif (root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p,q)
        elif(root.val < p.val and root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        







        