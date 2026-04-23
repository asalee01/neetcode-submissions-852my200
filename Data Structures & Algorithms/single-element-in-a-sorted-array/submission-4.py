class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #even ,odd to start off then when broken is odd, even.
        # if m is odd even then it is to the left. otherwise its to the right
        l, r = 0, len(nums)-1
        while(l <= r):
            m = (l + r) // 2
            isEven = (m % 2) == 0
            if isEven:
                if (m-1 >= 0 and nums[m -1] == nums[m]):
                    r = (m - 2)
                elif (m+1 <= r and nums[m+1] == nums[m]):
                    l = m + 2
                else:
                    return nums[m]
            else:
                if (m-1 >= 0 and nums[m -1] == nums[m]):
                    l = m + 1
                elif (m+1 <= r and nums[m+1] == nums[m]):
                    r = m - 1
                else:
                    return nums[m]
        return 0
