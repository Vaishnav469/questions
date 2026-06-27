class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevmax = intervals[0][1]
        res = 0

        for interval in intervals[1:]:
            if interval[0] >= prevmax:
                prevmax = interval[1]
            else:
                res += 1
                prevmax = min(interval[1], prevmax)
        return res
        