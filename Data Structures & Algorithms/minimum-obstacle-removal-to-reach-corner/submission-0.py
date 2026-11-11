from collections import deque
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque([(0,0,0)])
        visited = set([(0,0)])

        while q:
            ob, r, c = q.popleft()

            if r == rows-1 and c == cols - 1:
                return ob
            
            n0 = [1,-1,0,0]
            n1 =[0,0,1,-1]
            for x, y in zip(n0, n1):
                nx = r+x
                ny = c+y
                if (0<= nx < rows and 0 <= ny < cols and (nx,ny) not in visited):
                    if grid[nx][ny]:
                        q.append((ob+1, nx, ny))
                    else:
                        q.appendleft((ob, nx, ny))
                    visited.add((nx, ny))
                
        
    
