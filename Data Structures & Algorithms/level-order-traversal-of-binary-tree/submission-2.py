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
        q= deque()
        
        if (not root):
            return res
        
        q.append(root)

        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                if (node.left):
                    q.append(node.left)
                if (node.right):
                    q.append(node.right)
                level.append(node.val)
            res.append(level)
            
        return res
            
            

            

            

        