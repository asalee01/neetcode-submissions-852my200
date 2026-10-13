class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #find first interval with end_time >= new_start
        #after that we need to check all other intervals following for a merge
        intervals.append(newInterval)
        intervals.sort()

        updated = [intervals[0]]
        for start, end in intervals[1:]:
            if updated[-1][1] >= start:
                updated[-1][1] = max(updated[-1][1], end)
            else:
                updated.append([start, end])
        return updated
            
        