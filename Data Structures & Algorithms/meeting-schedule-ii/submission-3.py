"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key = lambda x: x.start)
        n = 0
        rooms = []
        
        for i in intervals:
            if rooms:
                earliest = heapq.heappop(rooms)
                if i.start < earliest:
                    heapq.heappush(rooms, earliest)
            heapq.heappush(rooms, i.end)
            n = max(n, len(rooms))
        
        return n
        
        