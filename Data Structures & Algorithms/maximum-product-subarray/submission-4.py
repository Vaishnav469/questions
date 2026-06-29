class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [[0, 0]] * n
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        maximum = 0
        for i in range(1, n):
            product1 = nums[i] * dp[i-1][0]
            product2 = nums[i] * dp[i-1][1]
            dp[i][0] = max(nums[i], product1, product2)
            dp[i][1] = min(nums[i], product1, product2)
            maximum = max(maximum, dp[i][0])
       
        return maximum



