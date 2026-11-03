class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxLen = 0
        r,c = len(matrix),len(matrix[0])
        dp = {}
        
        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]

            maxCurr = 1

            n0 = [1,-1,0,0]
            n1 = [0,0,1,-1]
            for x,y in zip(n0,n1):
                    if (0 <= i+x < r and 0 <= j+y < c and matrix[i+x][j+y] > matrix[i][j]):
                        maxCurr = max(maxCurr, 1+dfs(i+x, j+y))
            dp[(i,j)] = maxCurr
            return maxCurr
            

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxLen = max(dfs(i,j), maxLen)
        
        return max(dp[(i,j)] for (i,j) in dp)

    
        