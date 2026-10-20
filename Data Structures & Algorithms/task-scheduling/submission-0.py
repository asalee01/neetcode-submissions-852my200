import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        availability = deque()
        counts = {}
        for t in tasks:
            if not t in counts:
                counts[t] = 1
            else:
                counts[t] += 1
        for c in counts:
            maxHeap.append((-counts[c], 0))
        
        heapq.heapify(maxHeap)
        currCycle = 0

        while maxHeap or availability:
            currCycle += 1
            if maxHeap:
                val = heapq.heappop(maxHeap)
                if (val[0]+1 < 0):
                    newVal =(val[0]+1, currCycle + n)
                    availability.append(newVal)
            
            if availability and availability[0][1] <= currCycle:
                heapq.heappush(maxHeap, availability.popleft())
        return currCycle


        