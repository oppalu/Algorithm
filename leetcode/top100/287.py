# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
# prove that at least one duplicate number must exist. 
# Assume that there is only one duplicate number, find the duplicate one.

from collections import Counter
class Solution:
    def findDuplicate(self, nums):
        # 56 ms, 36.04% 
        counter = Counter(nums)
        node = counter.most_common(1)
        print(node[0][0])

Solution().findDuplicate([1,3,4,2,2])