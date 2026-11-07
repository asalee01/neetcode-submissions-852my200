class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0

        def dfs(i,j):
            c = 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0 
            n0 = [0,0,1,-1]
            n1 = [1,-1,0,0]
            for x, y in zip(n0, n1):
                if ((0 <= i+x < n) and (0 <= j+y < m) and grid[i+x][j+y] == 1):
                    c += 1 + dfs(i+x, j+y)
            return c

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = max(count, 1 + dfs(i,j))
        
        return count
        
        