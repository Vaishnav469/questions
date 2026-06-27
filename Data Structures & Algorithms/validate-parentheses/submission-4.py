class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(' : ')', '{' : '}', '[' : ']'}
        for i in s:
            if i in mapping.keys():
                stack.append(i)
            elif stack and mapping[stack[-1]] == i:
                stack.pop(-1)
            else:
                return False
        if not stack:
            return True
        else:
            return False
