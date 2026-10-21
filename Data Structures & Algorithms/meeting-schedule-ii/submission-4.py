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
        lists = defaultdict(int)

        for i in intervals:
            lists[i.start] += 1
            lists[i.end] -= 1
        
        res = 0
        c = 0
        for i in sorted(lists.keys()):
            c += lists[i]
            res = max(res, c)
        return res
        
        