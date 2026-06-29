class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            if s == "0":
                return 0
            else:
                return 1

        dp = [0] * (n+1)
        dp[-1] = 1
        if s[-1] != "0":
            dp[-2] = 1

        for i in range(n-2, -1, -1):
            if s[i] != "0":
                dp[i] += dp[i+1]
            if s[i] == "1" or (s[i] == "2" and s[i+1] <= "6"):
                dp[i] += dp[i+2]
        return dp[0]
            

