class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        word1 = [0] * 26
        word2 = [0] * 26

        for i in range(len(s)):
            word1[ord(s[i]) - ord('a')] += 1
            word2[ord(t[i]) - ord('a')] += 1

        for i in range(0, 26):
            if word1[i] != word2[i]:
                return False
        
        return True
