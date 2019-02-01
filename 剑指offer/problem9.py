# Fibonacci
# 扩展问题1[做法一样]：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# 扩展问题2[做法一样]:用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。pow(2,n-1)

class Solution:
    def Fibonacci1(self, n):
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        return self.Fibonacci1(n-1) + self.Fibonacci1(n-2)

    def Fibonacci2(self, n):
        if(n == 0):
            return 0
        if(n == 1):
            return 1

        pre = 0
        mid = 1
        res = 0
        for i in range(2,n+1):
            res = pre+mid
            pre = mid
            mid = res
        return res