class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        freq = defaultdict(int)
        i = 0
        j = 1
        length = 1
        maxlength = 1
        freq[s[i]] = 1
        while j < len(s) and i < j:
            if freq[s[j]] != 0 and j == i+1:
                freq[s[i]] -= 1
                freq[s[j]] += 1
                i += 1
                j += 1
                continue
            elif freq[s[j]] != 0:
                freq[s[i]] -= 1
                i += 1
                length -= 1
            else:
                freq[s[j]] += 1
                j += 1
                length += 1
            maxlength = max(maxlength, length)

        return maxlength

            