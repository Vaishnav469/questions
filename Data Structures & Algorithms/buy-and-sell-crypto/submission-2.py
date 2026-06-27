class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minimumtilldate = math.inf
        for i in prices:
            maximum = max(maximum, i - minimumtilldate)
            minimumtilldate = min(minimumtilldate, i)
        return maximum
