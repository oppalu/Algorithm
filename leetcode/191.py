# Number of 1 bits
# Write a function that takes an unsigned integer and return the number of '1' bits it has.

class Solution(object):
    def hammingWeight(self, n):
        # 思路：和n-1做异或会消掉一个末尾的1
        res = 0
        while n:
            n = (n-1) & n
            res = res + 1

        return res
    