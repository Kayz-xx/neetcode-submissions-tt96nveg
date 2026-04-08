class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        # we are currently pushing the next element and ignoring the last one
        for i in range(1, len(intervals)):
            last_end = res[-1][1]
            current_start, current_end = intervals[i]
            if current_start <= last_end:
                res[-1][1] = max(current_end, last_end) 
            else:
                res.append(intervals[i])
        return res