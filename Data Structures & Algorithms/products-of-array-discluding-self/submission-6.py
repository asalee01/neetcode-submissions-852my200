class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        zeroCnt = 0
        for num in nums:
            if (num == 0):
                zeroCnt +=1 
            else:
                product *= num

        if (zeroCnt > 1):
            return [0] * len(nums)

        for num in nums:
            val = 0
            if zeroCnt > 0:
                if num == 0:
                    val = product
                else:
                    val = 0
            else:
                val = product // num
            res.append(val)
        return res
        
        