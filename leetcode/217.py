# contains duplicate
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        # 60ms
        if not nums or len(nums) == 0:
            return False
        counter = Counter(nums)
        counter = counter.most_common()

        for i in counter:
            if i[1] > 1:
                return True

        return False

    def containsDuplicate2(self, nums):
        # 84ms
        return len(nums) != len(set(nums))

    def containsDuplicate3(self, nums):
        # 44ms
        numChecker = {}
        for num in nums:
            if num in numChecker:
                return True
            else:
                numChecker[num] = True
        return False


print(Solution().containsDuplicate([3,4]))