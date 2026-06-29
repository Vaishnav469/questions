class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        dp[-1][-1] = 1
        def valid(x, y):
            return x >= 0 and x < m and y >= 0 and y< n

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if valid(i+1, j):
                    dp[i][j] += dp[i+1][j]
                if valid(i, j+1):
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]

        