# house robber

# You plan to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, 
# determine the maximum amount of money you can rob tonight without alerting the police.

# input=[1,2,3,1], output=4
# input=[2,7,9,3,1], output=12

class Solution:
    # 40ms, 39.14%
    def rob(self, nums):
        if not nums:
            return 0

        dp = [0 for _ in range(len(nums)+1)]
        dp[1] = nums[0]

        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[-1]
        

nums = [2,7,9,3,1]
Solution().rob(nums)