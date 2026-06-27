class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                if not (res[-1][0] > interval[0] and  res[-1][1] > interval[1]) or res[-1][0] <= interval[1]:
                    res[-1][0] = min(res[-1][0], interval[0])
                    res[-1][-1] = max(res[-1][-1], interval[1])
                else:
                    res.append(interval)
        return res