# find the contiguous subarray within an array which has the largest product.

import sys
from functools import reduce
class Solution(object):
    def maxProduct(self, nums):
        # time limited
        if not nums:
            return 0

        product = 0 - sys.maxsize

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                temp = reduce(lambda x,y:x * y,nums[i:j+1])
                product = max(product, temp)
        return product

    def maxProduct2(self, nums):
        # 思路：保留最大最小，防止绝对值的问题。当前若为负则最大值为最小的*当前
        # 28 ms, 69.79% 
        max_v = min_v = res = nums[0]
        for i in range(1, len(nums)):
            max_v, min_v = max(nums[i], nums[i]*max_v, nums[i]*min_v), min(nums[i], nums[i]*max_v, nums[i]*min_v)
            res = max(max_v, res)
        return res

print(Solution().maxProduct2([-4,-3,-2]))