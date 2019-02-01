# top k frequent elements 要求O(n*logn)
# Given a non-empty array of integers, return the k most frequent elements.

from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        # 40ms, 68.93%
        counter = Counter(nums)

        counter = counter.most_common(k)
        res = []
        for i in counter:
            res.append(i[0])
        return res

nums = [1]
print(Solution().topKFrequent(nums, 1))
        