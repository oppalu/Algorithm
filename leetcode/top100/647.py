# Palindromic Substrings

# Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

class Solution:
    def isPalindromic(self, s):
        return list(s) == list(reversed(list(s)))

    def countSubstrings(self, s):
        # 12144 ms, 5.01% 
        res = 0
        if not s:
            return res
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindromic(s[i:j+1]):
                    res += 1
        return res

    def calculate(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.res += 1
            left -= 1
            right += 1

    def countSubstrings2(self, s):
        #  212 ms, 58.47% 
        if not s:
            return 0
        self.res = 0

        for i in range(len(s)):
            self.calculate(s, i, i)
            self.calculate(s, i, i+1)

        return self.res


print(Solution().countSubstrings2("abc")) #3
print(Solution().countSubstrings2("aaa")) #6