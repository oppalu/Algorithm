# 和为S的两个数字
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

import sys
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # 方法1，判断s-x是否在数组中
        multi = sys.maxsize
        res = []
        for i in array:
            if (tsum-i) in array and multi > i*(tsum-i):
                res = [i, tsum-i]
                multi = i*(tsum-i)

        return res

    def FindNumbersWithSum2(self, array, tsum):
        # 方法2，二分查找。从头和从尾，如果值大了尾部往前，否则头部往后
        multi = sys.maxsize
        i = 0
        j = len(array)-1
        res = []
        while i<j:
            if array[i]+array[j]==tsum:
                if multi > array[i]*array[j]:
                    res = [array[i], array[j]]
                    multi = array[i]*array[j]
                i += 1
                j -= 1
            elif array[i]+array[j]>tsum:
                j -= 1
            else:
                i += 1
        return res

arr = [1,2,4,7,11,15]
print(Solution().FindNumbersWithSum2(arr, 15))
