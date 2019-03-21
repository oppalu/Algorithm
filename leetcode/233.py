# number of digit 1
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

class Solution:
    def countDigitOne(self, n):
        # 参考剑指offer32题，看循环了几次
        result = 0
        if n < 1:
            return result

        base = 1
        round = n
        while round > 0:
            weight = (round % 10)
            round //= 10
            result += base*round
            if weight==1:
                result += (n%base)+1
            elif weight > 1:
                result += base
            base *= 10
        return result

print(Solution().countDigitOne(13))