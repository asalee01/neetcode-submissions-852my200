class Solution:
    def maxDifference(self, s: str) -> int:
        counts = {}
        odds = float("-inf")
        evens = float("inf")
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        for k,v in counts.items():
            if v % 2 == 0:
                evens = min(evens, v)
            else:
                odds = max(odds, v)
        return odds-evens