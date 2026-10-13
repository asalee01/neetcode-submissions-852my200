class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #find first interval with end_time >= new_start
        #after that we need to check all other intervals following for a merge
        res = []
        i = 0
        
        while (i < len(intervals) and intervals[i][1] < newInterval[0]):
            res.append(intervals[i])
            i += 1
        
        while(i< len(intervals) and newInterval[1] >= intervals[i][0]):
            newInterval[1] = max(intervals[i][1], newInterval[1])
            newInterval[0] = min(intervals[i][0], newInterval[0])
            i += 1
        res.append(newInterval)

        while(i < len(intervals)):
            res.append(intervals[i])
            i += 1
    
        return res
            
        