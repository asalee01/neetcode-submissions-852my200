# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #first node in preorder is the root, everything to the left is left
        #everything to the right is right subtree
        #to find root of subtrees, use inorder to find the first node to the
        #right and left of the current node. repeat this to the leaf nodes
        #this means the inorder to the right or left is out of bounds, so you
        #recurse back up
        map = {}
        for i, val in enumerate(inorder):
            map[val] = i  

        def build_tree(left, right, idx):
            if (left > right):
                return None
            root = preorder[idx]
            node = TreeNode(val=root)
            rootIdx= map[root]
            leftSize = rootIdx - left

            node.left = build_tree(left, rootIdx-1, idx+1)
            node.right = build_tree(rootIdx+1, right, idx+1+leftSize)

            return node

        return build_tree(0, len(preorder)-1, 0)

            
        