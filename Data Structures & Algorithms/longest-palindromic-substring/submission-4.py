class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = 0
        for i in range(len(s)):
            #odd length
            res, resLen = self.recurse(s, i, i, resLen, res)

            #even
            res, resLen = self.recurse(s, i, i+1, resLen, res)
        
        return res

        return self.recurse(s, 0, len(s)-1)

    def recurse(self, s, i, j, resLen, res):
        while (i >= 0 and  j < len(s)) and s[i] == s[j]:
            if (j-i+1) > resLen:
                resLen = j-i+1
                res = s[i:j+1]
            i -= 1
            j += 1
        
        return res, resLen

        
        