class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nNums = [1] + nums + [1]
        dp = [[0] * (n+2) for _ in range(n+2)]
    
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                for k in range(i,j+1):
                    v = nNums[i-1] * nNums[k] * nNums[j+1]
                    v += dp[i][k-1] + dp[k+1][j]
                    dp[i][j] = max(dp[i][j], v)
        return dp[1][n]