class Solution:
    def countSubstrings(self, s: str) -> int:
        reslen = 0
        resindx = 0
        count = 0
        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                if r - l + 1 > reslen:
                    reslen = r - l + 1
                    resindx = l
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                if r - l + 1 > reslen:
                    reslen = r - l + 1
                    resindx = l
                l -= 1
                r += 1
        
        return count