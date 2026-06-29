class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[-1] = True
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                j = len(word)
                if i + j <= n and word == s[i:i+j]:
                    dp[i] = dp[i+j]
                    if dp[i]:
                        break
        return dp[0]
                
                
