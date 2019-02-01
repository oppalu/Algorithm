# contains duplicate2
# Given an array of integers and an integer k, 
# find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] 
# and the absolute difference between i and j is at most k.

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        # 48ms
        res = {}
        for i in range(len(nums)):
            if nums[i] in res:
                if (i-res[nums[i]]) <= k:
                    return True
                else:
                    res[nums[i]] = i
            else:
                res[nums[i]] = i
        return False
    

print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(Solution().containsNearbyDuplicate([1,0,1,1], 1))
print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
print(Solution().containsNearbyDuplicate([99,99], 2))
