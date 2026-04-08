"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # okay so we are trying to find the number of rooms required 
        # we can reuse rooms when there is no conflict
        # assuming there are infinite rooms
        intervals.sort(key=lambda x: x.start)
        queue = []
        # ah i see the issue after testing
        # a room can get free which we then can use, we have no track of global rooms
        # simulating time and freeing up rooms is too complicated for this 
        # use some kind of queue for occupying different rooms
        # if we assign room to different intervals, do we compare with each one to add it to a correct room?
        # but that would become O(n^2) [thinking in terms of a map here is inefficient]
        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            if queue and queue[0] <= start:
                heapq.heappop(queue)
                heapq.heappush(queue, end)
            else:
                heapq.heappush(queue, end)
        
        return len(queue)