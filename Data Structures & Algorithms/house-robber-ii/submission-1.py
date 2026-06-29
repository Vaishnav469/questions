class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def dp(numbers, length):
            if length == 1:
                return numbers[0]
            dp = [0] * length
            dp[0] = numbers[0]
            dp[1] = max(numbers[0], numbers[1])
            for i in range(2, length):
                dp[i] = max(numbers[i] + dp[i-2], dp[i-1])
            return dp[-1]

        return max(dp(nums[:-1], n-1), dp(nums[1:], n-1))
