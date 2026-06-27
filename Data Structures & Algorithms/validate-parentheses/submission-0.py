class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in bracket_map.values():
                stack.append(i)
                continue
            if stack and bracket_map[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False

        