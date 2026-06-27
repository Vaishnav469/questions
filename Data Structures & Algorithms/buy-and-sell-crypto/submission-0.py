class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxp = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxp = max(profit, maxp)
            r += 1

        return maxp

        