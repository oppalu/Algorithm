# Product of Array Except Self

# Given an array nums of n integers where n > 1,  return an array output 
# such that output[i] is equal to the product of all the elements of nums except nums[i]. O(n)

class Solution:
    def productExceptSelf(self, nums):
        # 104 ms,  56.66% 
        res = [1 for _ in range(len(nums))]
        if not nums:
            return res

        temp = 1
        for i in range(1, len(nums)):
            temp *= nums[i-1]
            res[i] = temp

        temp = 1
        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i+1]
            res[i] *= temp
    
        return res

arr = [1,2,3,4]
print(Solution().productExceptSelf(arr))