# contains duplicate3
# Given an array of integers, find out whether there are two distinct indices i and j in the array 
# such that the absolute difference between nums[i] and nums[j] is at most t 
# and the absolute difference between i and j is at most k.

class Solution:
    def containsNearbyAlmostDuplicate0(self, nums, k, t):
        # time limited
        res = {}
        for i in range(len(nums)):
            min_index = max(0, i-k)
            max_index = min(len(nums), i+k+1)
            for j in range(min_index, max_index):
                if nums[j] in res and i != j and abs(nums[i]-nums[j]) <= t:
                    return True
                res[nums[i]] = i
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # 思路：桶排序
        # suppose we have consecutive buckets covering the range of nums with each bucket a width of (t+1).
        # If there are two item with difference <= t, then the 2 item in the same/neighbor buckets
        if k<1 or t < 0:
            return False
        res = {}
        w = t+1
        for i in range(len(nums)):
            temp = nums[i] / w
            if temp in res:
                return True

        # d = {}
        # w = t + 1
        # for i in xrange(n):
        #     m = nums[i] / w
        #     if m in d:
        #         return True
        #     if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
        #         return True
        #     if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
        #         return True
        #     d[m] = nums[i]
        #     if i >= k: del d[nums[i - k] / w]
        # return False



print(Solution().containsNearbyAlmostDuplicate([1,2,3,1],3,0))
print(Solution().containsNearbyAlmostDuplicate([1,0,1,1], 1,2))
print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))


