class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    q.append((i,j))
                    grid[i][j] = "2"
                    count += 1
                
                while(q):
                    x,y = q.pop()
                    directions = [[1,0], [-1,0], [0,1],[0,-1]]
                    for dr, dc in directions:
                        r = int(x) +dr
                        c= int(y) + dc
                        if r < len(grid) and r >= 0 and c < len(grid[0]) and c >= 0 and (grid[r][c]) == "1":
                            q.append((str(r),str(c)))
                            grid[r][c] = "2"
                    
        return count
        