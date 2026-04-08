class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            last_end = res[-1][1]
            current_start, current_end = intervals[i]
            if current_start <= last_end:
                res[-1][1] = max(current_end, last_end) 
            else:
                res.append(intervals[i])
        return res