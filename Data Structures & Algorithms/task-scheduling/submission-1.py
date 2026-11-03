import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        availability = deque()
        counts = {}

        for task in tasks:
            if not task in counts:
                counts[task] = 1
            else:
                counts[task] += 1
        
        for c in counts:
            heap.append((-counts[c], 0))

        heapq.heapify(heap)
        cycle = 0

        while heap or availability:
            cycle += 1
            if heap:
                val = heapq.heappop(heap)

                if(val[0]+1 < 0):
                    new = (val[0]+1, cycle+n)
                    availability.append(new)
            
            if availability and availability[0][1] <= cycle:
                heapq.heappush(heap, availability.popleft())
        
        return cycle
