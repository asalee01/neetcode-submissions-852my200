class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #0 == free, 1 == hold, 2 == sold, 3 == cooldown
        n = len(prices)
        dp = [[float("-inf") for _ in range(len(prices))] for _ in range(4)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(1,n):
            dp[0][i] = max(dp[0][i-1], dp[3][i-1])
            dp[1][i] = max(dp[0][i] - prices[i], dp[1][i-1])   
            dp[2][i] = dp[1][i-1]+ prices[i]
            dp[3][i] = dp[2][i-1]
        return max(dp[0][n-1], dp[2][n-1], dp[3][n-1])