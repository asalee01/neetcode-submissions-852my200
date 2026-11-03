class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxLen = 0
        dp = {}
        
        def dfs(i, j , prev):
            if (i,j) in dp:
                return dp[(i,j)]
            maxCurr = 1
            if prev >= matrix[i][j]:
                return 0
            r,c = len(matrix),len(matrix[0])
            n0 = [1,-1,0,0]
            n1 = [0,0,1,-1]
            for x,y in zip(n0,n1):
                    if (0 <= i+x < r and 0 <= j+y < c and matrix[i+x][j+y] > matrix[i][j]):
                        curr =  1 + dfs(i+x, j +y, matrix[i][j])
                        maxCurr = max(maxCurr, curr)
            dp[(i,j)] = maxCurr
            return maxCurr
            

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxLen = max(dfs(i,j, -1), maxLen)
        
        return max(dp[(i,j)] for (i,j) in dp)

    
        