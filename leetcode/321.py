# create maximum number

# Given two arrays of length m and n with digits 0-9 representing two numbers. 
# Create the maximum number of length k <= m + n from digits of the two. 
# 【The relative order of the digits from the same array must be preserved】. Return an array of the k digits.
# ex:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# Output:
# [9, 8, 6, 5, 3]

class Solution:

    def maxNumber(self, nums1, nums2, k) -> 'List[int]':
        

nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]

num3 = [6, 7]
num4 = [6, 0, 4]
print(Solution().maxNumber(nums1, nums2, 5))