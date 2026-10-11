class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp0 = [0] * (n)
        dp0[1] = nums[0]

        for i in range(2, len(dp0)):
            dp0[i] = max(dp0[i-1], nums[i-1] + dp0[i-2])

        dp1 = [0] * (n)
        dp1[1] = nums[1]

        for i in range(2, len(dp1)):
            dp1[i] = max(dp1[i-1], nums[i] + dp1[i-2])
        

        return max(dp0[n-1], dp1[n-1])
        #but this does not account for the last index being reachable.
        #so if you started with picking the last index (len(nums) -1) then you
        #cannot pick idx 0... so 

        