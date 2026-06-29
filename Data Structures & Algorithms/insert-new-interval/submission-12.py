class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        if not intervals:
            result.append(newInterval)
            return result

        i, j = 0, len(intervals) - 1
        while i <= j:
            mid = (i+j)//2
            if intervals[mid][0] < newInterval[0]:
                i = mid + 1
            else:
                j = mid - 1
        intervals.insert(i, newInterval)
           

            
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result

