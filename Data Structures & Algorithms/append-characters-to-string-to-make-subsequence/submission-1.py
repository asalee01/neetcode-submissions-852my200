class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx = 0
        for i in s:
            if idx < len(t) and i == t[idx]:
                idx += 1
        return len(t) - idx
