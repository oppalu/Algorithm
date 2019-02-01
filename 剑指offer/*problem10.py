# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
# *思路：把一个整数-1，再和原整数做与运算，这就会把整数最右面一个1变成0
# 思路2：用1跟每一位做与看是否为1


class Solution:
    def NumberOf1(self, n):
        # write code here
        res = 0
        while n:
            n = (n-1) & n
            res = res +1

        return res

print(Solution().NumberOf1(11))