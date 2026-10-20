# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #keep track of path to reach p and path to reach q
        paths = [[] for i in range(2)]

        def dfs(node, target, id):
            if not node:
                return False

            paths[id].append(node)
            if (node.val == target.val):
                return True

            if dfs(node.left, target, id) or dfs(node.right, target, id):
                return True
            
            paths[id].pop()
            return False
        
        dfs(root, p, 0)
        dfs(root, q, 1)

        lca = None
        for a, b in zip(paths[0], paths[1]):
            if a is b:
                lca = a
            else:
                break
        return lca





        