class Solution:
    def uniquePaths(self, m:int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1,-1):
                if i == m-1and j == n-1:
                    dp[i][j] = 1
                else:
                    if i+1 < m and dp[i+1][j]:
                        dp[i][j] += dp[i+1][j]
                    if j+1 < n and dp[i][j+1]:
                        dp[i][j] += dp[i][j+1]
        return dp[0][0]


        