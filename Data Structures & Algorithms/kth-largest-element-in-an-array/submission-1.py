import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heap.append(-1*n)
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -1*heap[0] 