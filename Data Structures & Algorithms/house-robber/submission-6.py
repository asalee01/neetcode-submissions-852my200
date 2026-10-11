class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {-1: 0, 0: nums[0]}
        def nextRob(nums, i):
            if i == -1:
                return 0
            if i in memo:
                return memo[i]
            
            a1 = nums[i] + nextRob(nums, i-2)
            a2 = nextRob(nums, i-1)
            val = max(a1,a2)
            memo[i] = val
            return val
        
        return nextRob(nums, len(nums)-1)
            
            
        