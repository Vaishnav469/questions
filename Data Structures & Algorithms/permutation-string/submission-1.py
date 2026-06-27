class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        string1 = [0] * 26
        string2 = [0] * 26

        for s in s1:
            string1[ord(s) - ord('a')] += 1
        
        l = 0
        r = l + len(s1) - 1
        
        #frequency of stuff in sliding window
        for i in range(r+1):
            string2[ord(s2[i]) - ord('a')] += 1
            
        while r < len(s2):
            if string1 == string2:
                return True
            else:
                string2[ord(s2[l]) - ord('a')] -= 1
                l += 1
                r += 1
                if r < len(s2):
                    string2[ord(s2[r]) - ord('a')] += 1
                else:
                    return False
        return False






        