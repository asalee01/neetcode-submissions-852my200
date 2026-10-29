class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #can have a tree with root for each char in the shorter of t1 and t2
        #example t1 = "cat" and t2 = "crabt"
        # 3 root trees will be made c, a, and t.
        #if c is a match at any point of t2 then you increment both t1 and t2
        #do this until you are either at the end of t1 or t2
        #then repeat for the other 2 letters, store each length in a res array
        #return largest length
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]


        