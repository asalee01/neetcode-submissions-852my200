class Solution:
    def maxDifference(self, s: str) -> int:
        counts = {}
        odds = {}
        evens = {}
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        for k,v in counts.items():
            if v % 2 == 0:
                evens[k] = v
            else:
                odds[k] = v
        return max(odds.values()) - min(evens.values())