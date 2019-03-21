# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000
# (参考647)
class Solution(object):
    def calculate(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if len(self.res) < right-left:
            self.res = s[left+1:right]

    def longestPalindrome(self, s):
        # 792 ms, 69.58%
        self.res = ''
        if not s:
            return self.res
        
        for i in range(len(s)):
            self.calculate(s, i, i)
            self.calculate(s, i, i+1)
        return self.res

print(Solution().longestPalindrome('abba'))