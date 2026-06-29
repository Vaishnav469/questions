class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[-1] = True
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                j = len(word)
                if i + j > n:
                    continue
                if word == s[i:i+j]:
                    dp[i] = dp[i+j] or dp[i]
        return dp[0]
                
                
