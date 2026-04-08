class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        p = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    p += self.checkborder(grid, i ,j)
        return p

    def checkborder(self, grid, i, j):
        rows, cols = len(grid), len(grid[0])
        s = 0
        if (i + 1 >= rows or grid[i+1][j] == 0):
            s += 1
        if (j + 1 >= cols or grid[i][j+1] == 0):
            s += 1
        if (i - 1 < 0 or grid[i-1][j] == 0):
            s += 1    
        if (j - 1 < 0 or grid[i][j-1] == 0):
            s += 1
        return s