class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
                else:
                    continue
        print(dp)
        if dp[amount] == float("inf"):
            return -1 
        else:
            return dp[amount]

        
        
