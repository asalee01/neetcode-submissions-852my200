import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [float('-inf')] * k

        for n in nums:
            v = heapq.heappop(heap)
            if v < n:
                heapq.heappush(heap, n)
            else:
                heapq.heappush(heap, v)
        return heap[0]