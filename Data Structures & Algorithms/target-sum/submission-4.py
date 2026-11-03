class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # we care about the different paths and what we are repeatedly calculating
        dp = {}

        n = len(nums)
        def dfs(total, i):
            if i == n:
                if total == target:
                    return 1
                else: 
                    return 0
            if (total, i) in dp:
                return dp[(total, i)]
            else:
                dp[(total, i)] = dfs(total+nums[i], i+1) + dfs(total-nums[i], i+1)
                return dp[(total,i)]
            
            

        
        return dfs(0,0)

        
        