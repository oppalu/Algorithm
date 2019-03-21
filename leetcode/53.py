# maximum subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

import sys
class Solution:
    def maxSubArray(self, nums):
        res = [0 for i in range(len(nums))]
        result = 0 - sys.maxsize

        for i in range(len(nums)):
            res[i] = nums[i] + max(0, res[max(0,i-1)])
            result = max(result, res[i])

        return result


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(arr))