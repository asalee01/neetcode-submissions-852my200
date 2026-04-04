class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxim, curr = 0, 0
        for n in nums:
            if n != 1:
                curr = 0
                continue
            curr += 1
            if curr > maxim:
                maxim = curr
        return maxim
        