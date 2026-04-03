class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for i in s[::-1]:
            if (i == " " and l == 0):
                continue
            if (i == " "):
                break
            l += 1
        return l
        