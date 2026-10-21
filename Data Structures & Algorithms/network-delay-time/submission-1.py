import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #dijkstra's lowk useful here....
        dist = [float("inf") if i != k else 0 for i in range(n+1)]
        graph = [[] for _ in range(n+1)]
        for start, end,cost in times:
            graph[start].append((end, cost))
        minHeap = [(0,k)]

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            for c in graph[node]:
                end, price = c
                new_cost = cost + price
                if new_cost < dist[end]:
                    dist[end] = new_cost
                    heapq.heappush(minHeap, (new_cost, end))
        
        return -1 if float("inf") in dist[1:] else max(dist[1:])