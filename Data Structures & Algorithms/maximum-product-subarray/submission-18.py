class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minProd,maxProd = 1,1 

        for i in range(len(nums)):
            tmp = maxProd
            maxProd = max(nums[i], maxProd*nums[i], minProd*nums[i])
            minProd = min(nums[i], tmp*nums[i], minProd*nums[i])
            res= max(res, maxProd)
        return res
