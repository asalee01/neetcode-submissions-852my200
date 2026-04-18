class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (s == t):
            return True
        vals1, vals2 = {}, {}
        for i in range(len(s)):
            if (s[i] in vals1 and not t[i] == vals1[s[i]]):
                return False
            if (t[i] in vals2 and not s[i] == vals2[t[i]]):
                return False
            vals1[s[i]] =  t[i]
            vals2[t[i]] = s[i]
                
        return True