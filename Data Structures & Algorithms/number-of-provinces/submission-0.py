class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #given adjacency matrix want to find all connected components
        count = 0
        visited = set()
        #iterate through each city
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1

                visited.add(i)
                q = deque()
                q.append(i)

                while q:
                    curr = q.popleft()

                    for n in range(len(isConnected[curr])):
                        if (not n in visited) and (isConnected[curr][n] == 1):
                            q.append(n)
                            visited.add(n)
        return count


            
    
        
        