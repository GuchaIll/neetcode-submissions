"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 0:
            return 0

        intervals.sort(key = lambda x: x.start)
        rooms = [intervals[0].end]
        for i in range(1, len(intervals)):
            interval = intervals[i]

            #if the earliest end time is less than start time of current interval, occupy same room by replacement
            if rooms[0] <= interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)

        return len(rooms)
            