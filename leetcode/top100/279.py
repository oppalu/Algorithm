# perfect squares
# Given a positive integer n, find the least number of perfect square numbers
#  (for example, 1, 4, 9, 16, ...) which sum to n.

# n=12,output=3(4+4+4)
# n=13,output=2(4+9)

from math import floor, sqrt
import sys

class Solution:

    def find(self, n):
        if n in self.data:
            return 1
        if self.dp[n] != -1:
            return self.dp[n]

        ans = sys.maxsize
        for i in self.data:
            if i < n:
                ans = min(ans, 1+self.find(n-i))
        self.dp[n] = ans
        return ans
        
    def numSquares(self, n: int) -> int:
        # 法一：先找到所有的完全平方数，然后递归(超时)
        if n == 0:
            return 0
        self.dp = [-1 for _ in range(n+1)]
        self.data = []
        for i in range(1, floor(sqrt(n))+1):
            self.data.append(i*i)

        return self.find(n)

    def numSquares2(self, n: int) -> int:
        # 法2：思想类似，做法简便。dp[n] = Min{dp[n-i*i]+1}   36.91%
        if n == 0:
            return 0
        dp = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            ans = sys.maxsize
            for j in range(1, floor(sqrt(i))+1):
                ans = min(ans, dp[i-j*j]+1)
            dp[i] = ans
        return dp[-1]

print(Solution().numSquares2(56))
