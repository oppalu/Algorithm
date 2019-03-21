# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

import sys
class Solution:
    def coinChange(self, coins, amount):
        # 1264 ms, 60.06% 
        dp = [sys.maxsize for _ in range(amount)]
        dp = [0]+dp

        for i in range(1, amount+1):
            min_v = sys.maxsize
            for j in coins:
                if i >= j:
                    min_v = min(min_v, dp[i-j])
            dp[i] = min_v + 1
        
        res = dp[-1] if dp[-1] < sys.maxsize else -1
        return res

coins = [1, 2, 5]
amount = 11
print(Solution().coinChange([2], 3))
        

