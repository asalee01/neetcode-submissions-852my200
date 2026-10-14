class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        #compute all two sums and if the third index
        for i in range(len(nums)):
            visited = {}
            target = (nums[i] * -1)
            #two sum now
            for j in range(i+1, len(nums)):
                check = target - nums[j]
                if check in visited:
                    k = nums[visited[check]]
                    res.add((nums[i], nums[j], k))
                else:
                    visited[nums[j]]= j
        result = [list(t) for t in res]
        return list(result)

                
        