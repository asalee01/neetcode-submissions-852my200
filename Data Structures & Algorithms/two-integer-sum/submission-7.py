class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for idx, val in enumerate(nums):
            vals[val] = idx
        print(vals)
        for i in range(len(nums)):
            check = target - nums[i]
            if check in vals and vals[check] != i:
                return [i, vals[check]]
        return []
        