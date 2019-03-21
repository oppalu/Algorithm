# generate Parenthesis
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n):
        self.dp = [[] for _ in range(n)]
        self.dp[0] = ['()']

        for i in range(1, n):
            pre = self.dp[i-1]
            for s in pre:
                self.dp[i].append('()'+s)
                self.dp[i].append(s+'()')
                self.dp[i].append('('+s+')')

        return list(set(self.dp[n-1]))


res = Solution().generateParenthesis(4)
print(res)
