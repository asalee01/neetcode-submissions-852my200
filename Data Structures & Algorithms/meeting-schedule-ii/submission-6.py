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
        #earliest starting times min heap
        #end time matters as that determines whether the room
        #is available, we keep track of rooms that are currently being used with
        #earliest end time  
        intervals.sort(key=lambda x: x.start)
        rooms = []
        cnt = 0

        for interval in intervals:
            if rooms and (rooms[0] <= interval.start):
                    heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
            cnt = max(cnt, len(rooms))
        
        return cnt
                
        
        