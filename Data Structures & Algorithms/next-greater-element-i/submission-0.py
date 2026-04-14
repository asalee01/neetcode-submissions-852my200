class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums1)):
            idx = 0
            for j in range(len(nums2)):
                if (nums1[i] == nums2[j]):
                    for x in range(j+1,len(nums2)):
                        if nums1[i] < nums2[x]:
                            idx = nums2[x]
                            break
            if (idx == 0):
                arr.append(-1)
            else:
                arr.append(idx)
        return arr
            
        