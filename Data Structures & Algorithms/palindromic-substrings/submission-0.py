class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                currS = s[i:j+1]
                revS = currS[::-1]
                if currS == revS and len(currS) > 0:
                    c += 1
        
        return c
        