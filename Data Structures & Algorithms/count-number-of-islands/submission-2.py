class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs 

        def dfs(row, col):
            n = len(grid)
            m = len(grid[0])
            if grid[row][col] == "0":
                return
            else:
                neighbors0 = [0,1,-1,0]
                neighbors1 = [1,0,0,-1]
                grid[row][col] = "0"
                for i in range(len(neighbors0)):
                    r_new = row + neighbors0[i]
                    c_new = col + neighbors1[i]
                    if (0 <= r_new < n) and (0 <= c_new < m):
                        dfs(r_new, c_new)
            return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count
        