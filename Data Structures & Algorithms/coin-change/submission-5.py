class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use a dictionary for easier min operations?
        if amount == 0:
            return 0
        dp = [-1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i - j >= 0:
                    if dp[i] == -1 and dp[i-j] != -1:
                        dp[i] = dp[i-j] + 1
                    elif dp[i-j] != -1:
                        dp[i] = min(dp[i], dp[i-j] + 1)
                    else:
                        continue
       
        return dp[amount]
      
        


