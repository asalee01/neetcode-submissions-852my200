class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #goal to get from [0][0] to [n-1][n-1]
        #can go 8 directions from each point
        # 0 is unvisited, if 1 cannot traverse, dfs might be better
        #we dont need a visited array as the path may be shorter
        g =len(grid)
        if grid[0][0] or grid[g-1][g-1]:
            return -1
        
        q = []
        q.append((0,0))
        grid[0][0] = 1
        while q:
            i, j  = q.pop(0)
            v = grid[i][j]

            if i == g-1 and j == g-1:
                return v

            n0 = [0,1,-1]
            n1 = [0,1,-1]

            for nx in n0:
                for ny in n1:
                    if 0 <= i+nx < g and 0 <= j+ny < g and grid[i+nx][j+ny] == 0 and (not i == i+nx or not j+ny == j):
                        grid[i+nx][j+ny] = v+1
                        q.append((i+nx, j+ny))
            
        return -1
                    
        