# Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s: str) -> bool:
        # 40ms, 51.62%
        if not s:
            return True
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif i == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif i == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
        
        if not stack:
            return True
        return False


print(Solution().isValid('}'))