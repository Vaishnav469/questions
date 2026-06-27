class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1
        s = s.lower()
        while i < j:
            if not ((s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9')):
                i += 1
                continue
            elif not ((s[j] >= 'a' and s[j] <= 'z') or (s[j] >= '0' and s[j] <= '9')):
                j -= 1
                continue
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

