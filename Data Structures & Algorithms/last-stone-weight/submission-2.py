import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #use a max heap
        #if len >= 2, pop the last two subtract them and whichever one is left is
        # is added back to the heap
        #if len < 2: we know that only 1 stone is left return that
        #so a while loop

        neg = [-1 * n for n in stones]
        heapq.heapify(neg)
        while(len(neg) >= 2):
            maxVal = -1 * heapq.heappop(neg)
            secondMax = -1 * heapq.heappop(neg)
            if (maxVal - secondMax):
                heapq.heappush(neg, secondMax - maxVal)

        return -1 * heapq.heappop(neg) if len(neg) > 0 else 0
        