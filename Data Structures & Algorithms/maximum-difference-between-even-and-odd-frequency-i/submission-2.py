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
        for k in counts:
            if counts[k] % 2 == 0:
                evens = min(evens, counts[k])
            else:
                odds = max(odds, counts[k])
        return odds-evens