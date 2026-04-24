class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxS = 0
        for i in range(len(nums)):
            if nums[maxS] < nums[i]:
                maxS = i
        return maxS
        