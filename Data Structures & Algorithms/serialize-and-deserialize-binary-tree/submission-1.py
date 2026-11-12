# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec: 
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []
        def preorder(node):
            if (not node):
                serialized.append('N')
                return
            serialized.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(serialized)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        self.i = 0

        def build():
            if nodes[self.i] =='N':
                self.i+= 1
                return None
            node = TreeNode(val=int(nodes[self.i]))
            self.i+= 1
            node.left = build()
            node.right = build()
            return node
        return build()


