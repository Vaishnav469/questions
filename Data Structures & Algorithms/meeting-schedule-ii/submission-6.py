"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        prevmax = [intervals[0].end]
        res = 1
        for interval in intervals[1:]:
            fits = False
            for i in range(len(prevmax)):
                if interval.start < prevmax[i]:
                    continue
                else:
                    fits = True
                    prevmax[i] = interval.end
                    break
            if not fits:
                res += 1
                prevmax.append(interval.end)
                    
        return res
        