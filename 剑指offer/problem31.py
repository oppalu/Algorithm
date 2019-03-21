# 连续子数组的最大和
# 输入一个整形数组，数组中一个/连续多个整数组成一个子数组。求所有子数组和的最大值

import sys
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # 如果前一次计算的和<=0，则从当前数字重新计算，否则加上当前数字的值。每次运算后进行与最大值的比较考虑替换
        if not array or len(array) == 0:
            return 0

        result = 0-sys.maxsize
        current = 0
        for i in array:
            if current <= 0:
                current = i
            else:
                current += i

            if current > result:
                result = current
        return result

    def FindGreatestSumOfSubArray2(self, array):
        # 动态规划思想：假设f(i)表示以第i个数字结尾的子数组的最大和，则
        # 当i=0或f(i-1)<=0时，f(i) = array[i]。否则f(i)=array[i]+f(i-1)
        if not array or len(array) == 0:
            return 0
        res = 0-sys.maxsize
        dp = [0 for i in range(len(array))]

        for i in range(len(array)):
            dp[i] = dp[i-1]+array[i] if dp[i-1]>0 or i==0 else array[i]
            print(dp)
            res = max(dp[i], res)

        return res


arr = [1,-2,3,10,-4,7,2,-5]
arr2 = [2,8,1,5,9]
print(Solution().FindGreatestSumOfSubArray2(arr2))