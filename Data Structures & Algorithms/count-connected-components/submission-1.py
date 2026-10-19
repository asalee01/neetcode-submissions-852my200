from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #bfs in my opinion
        #start at the start of edges, append its edges to the queue, we can 
        # use a helper method for the bfs. so each time it is called, we have a
        # for loop that calls bfs for every edge if it has been visited
        visited = []
        q = deque()
        count = 0
        graph = [[] for _ in range(n)]
        for l, r in edges:
            graph[l].append(r)
            graph[r].append(l)

        def dfs(node):
            q.append(node)
            while q:
                x = q.popleft()
                visited.append(x)

                for i in graph[x]:
                    if not i in visited:
                        dfs
                        q.append(i)
            return
            
        
        for i in range(n):
            if not i in visited:
                dfs(i)
                count += 1
        
        return count