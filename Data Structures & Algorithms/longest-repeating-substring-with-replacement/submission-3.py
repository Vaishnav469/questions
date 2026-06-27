class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxfreq = 0 # max character of window
        res = 0 # result
        l = 0
        for r, n in enumerate(s):
            count[n] += 1
            maxfreq = max(maxfreq, count[n])

            if (r - l + 1) - maxfreq - k > 0:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
