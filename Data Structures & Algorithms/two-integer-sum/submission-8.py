class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for idx, val in enumerate(nums):
            check = target - val
            if check in vals:
                return [vals[check], idx]
            vals[val] = idx
        return []
        