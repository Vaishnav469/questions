class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0;
        j = len(s) - 1

        while i < len(s):
            if not (ord(s[i].lower()) <= ord('z') and ord(s[i].lower()) >= ord('a')) and not (ord(s[i].lower()) <= ord('9') and ord(s[i].lower()) >= ord('0')):
                i += 1
                continue
            if not (ord(s[j].lower()) <= ord('z') and ord(s[j].lower()) >= ord('a')) and not  (ord(s[j].lower()) <= ord('9') and ord(s[j].lower()) >= ord('0')):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True