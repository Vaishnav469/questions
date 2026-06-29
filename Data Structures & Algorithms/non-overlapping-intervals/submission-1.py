class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[0])
        prevmax = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            if prevmax <= interval[0]:
                prevmax = interval[1]
            else:
                res += 1
                prevmax = min(prevmax, interval[1])
        return res