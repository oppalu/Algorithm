# 替换空格，从前往后将空格替换成%20
# (其他思路：先遍历确定替换后的长度，然后一个指针指向新的尾部一个指针指向原字符串尾部， 从后面开始移动)
# 举一反三：有两个排序的数组A1, A2,内存在A1的末尾有足够多的空余空间容纳A2.实现一个函数把A2中的数字插入到A1中且所有数字是排序的

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res