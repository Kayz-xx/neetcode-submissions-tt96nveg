"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # we can sort by start time
        # if end time of previous element is greater
        # than start time of next element, we have a conflict
        intervals.sort(key=lambda interval: interval.start)
        # what if there is conflict between 1 and 3 but not 2? is this possible?
        # no because it is sorted
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        
        return True