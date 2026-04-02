class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robHelper(nums[:-1]), self.robHelper(nums[1:]))

    
    def robHelper(self, nums):
        l, r = 0, 0
        for n in nums:
            temp = max(n + l, r)
            l = r
            r = temp
        return r

