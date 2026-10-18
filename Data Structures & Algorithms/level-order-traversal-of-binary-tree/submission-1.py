# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#this is bfs so while we will use a queue and there will be no cycles as a tree
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(root):
            q = []
            if not root:
                return
            q.append(root)
            while(len(q)>0):
                node = q[0]
                level_size=len(q)
                level = []
                for i in range(level_size):
                    node = q[0]
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level.append(q.pop(0).val)
                res.append(level)
            return
        dfs(root)
        return res
            
            

            

            

        