from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #parent array to keep track of each node's parent
        #rank array to keep track of its connected component count
        parent = [i for i in range(n)]
        rank = [1] * n
        count = 0
        
        def find(n):
            curr = n
            while curr != parent[curr]:
                parent[curr]= parent[parent[curr]]
                curr = parent[curr]
            return curr
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                p1, p2 = p2, p1
            
            parent[p2] = p1
            rank[p1] += rank[p2]
            return True
        
        res = n
        for l, r in edges:
            if union(l,r):
                res -= 1
        
        return res