class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            dp[i][i+1] = (s[i] == s[i+1])

        for i in range(n-1,-1,-1):
            for j in range(n-1, i, -1):
                if s[i] == s[j] and j-i>1:
                    dp[i][j] = dp[i+1][j-1]
        
        for i in range(n):
            for j in range(n):
                if dp[i][j] == True:
                    c+=1
        
        return c
                

        

        