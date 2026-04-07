class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #needs to be in order for it to be a subsequence
        #so we iterate through t and for every time s's char is present from zero
        # we increment t's index to a value. at the end of the loop
        #we should output the diff between len(t) and idx
        idx = 0
        for i in s:
            if idx < len(t) and i == t[idx]:
                idx += 1
        return len(t) - idx
