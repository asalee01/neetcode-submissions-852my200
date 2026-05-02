class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        cnt, numFresh = 0, 0
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == 1):
                    numFresh += 1
                if (grid[i][j] == 2):
                    q.append((i,j))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and numFresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row,col))
                    numFresh -= 1
            cnt += 1
                
        if numFresh ==  0:
            return cnt
        else:
            return -1