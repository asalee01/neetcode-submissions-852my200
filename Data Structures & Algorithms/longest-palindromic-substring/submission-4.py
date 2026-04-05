class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            oVal = self.findPal( s, i, i)
            eVal = self.findPal(s, i, i+1)
            if len(oVal) > len(res):
                 res = oVal
            if len(eVal) > len(res):
                res = eVal
        return res
        

    def findPal(self, s, l, r):
        val = ''
        n = 0
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            if(r - l + 1 > n):
                val = s[l:r+1]
                n = r - l + 1
            l -= 1
            r += 1
        return val
    

