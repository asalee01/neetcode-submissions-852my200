class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = []
        for i in range(len(nums)):
            if nums[i] in vals:
                return True
            vals.append(nums[i])
        return False
        