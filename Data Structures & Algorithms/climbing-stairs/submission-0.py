class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        i = 1
        j = 1

        h = n-1
        while h > 0:
            k = i + j
            i = j
            j = k
            h -= 1
        return k


