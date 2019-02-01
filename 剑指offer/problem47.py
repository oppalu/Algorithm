# 不用加减乘除做加法
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

class Solution:
    def Add(self, num1, num2):
        # write code here
        return sum([num1,num2])

    def Add2(self, num1, num2):
        # 思路：位运算，只有1+1的时候会进位其他与异或结果相同。
        # 分三步，1是相加但不进位(异或)，2是记下进位情况(按位与，左移一位)，3是2者相加。然后重复直到进位为0
        return num1 if num2 == 0 else self.Add2(num1 ^ num2, (num1 & num2) << 1)