class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        setS = [0] * 26
        setT = [0] * 26
        for i in range(0, len(s)):
            setS[ord(s[i]) - ord('a')] += 1
            setT[ord(t[i])- ord('a')] += 1
        for i in range(0, 26):
            if setS[i] != setT[i]:
                return False
        return True
