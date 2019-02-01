# 左旋转字符串
# ex: 字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        data = s + s
        length = len(s)
        return data[n:n+length]

print(Solution().LeftRotateString("abcXYZdef", 3))
