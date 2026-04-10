class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        ma, mi = 1, 1
        for n in nums:
            tmp = n * ma
            ma = max(n * ma, n* mi, n)
            mi = min(tmp, n* mi, n)
            res = max(res, ma)
        return res



          
        