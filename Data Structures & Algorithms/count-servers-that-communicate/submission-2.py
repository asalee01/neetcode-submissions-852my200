class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        #create a helper function to check if t/b/r/l exist
        #then check if one of them has connection, if they do add 1.
        servers = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    servers += self.checkBorder(i, j, grid)
        return servers


    def checkBorder(self, i, j, grid) -> int:
        for x in range(len(grid)):
            if grid[x][j] == 1 and not i == x:
                return 1
        for y in range(len(grid[0])):
            if grid[i][y] == 1 and not j == y:
                return 1
        
        return 0
            
        