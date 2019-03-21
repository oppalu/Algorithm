# Regular Expression Matching
# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

class Solution:
    def isMatch(self, s, p):
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) != 0 and len(p) == 0:
            return False

        if len(p) > 1 and p[1] == '*':
            # 匹配0个
            if len(s) == 0 or (s[0] != p[0] and p[0] != '.'):
                return self.isMatch(s[:], p[2:])
            else:
                # 分别是匹配多个，匹配1个&匹配0个
                return self.isMatch(s[1:], p[:]) or self.isMatch(s[1:], p[2:]) or self.isMatch(s[:], p[2:])
        else:
            # 不是*直接匹配
            if len(s) != 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False


print(Solution().isMatch('aa', 'a'))
print(Solution().isMatch('aa', 'a*'))
print(Solution().isMatch('a', 'a*a'))
print(Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))

