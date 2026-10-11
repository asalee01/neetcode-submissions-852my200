class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def robber(nums):
            p, c = 0, 0

            for num in nums:
                p, c = c, max(c, num + p)
            return c
        return max(robber(nums[1:]), robber(nums[:-1]))

        