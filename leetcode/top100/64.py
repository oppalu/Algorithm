# Given a m x n grid with non-negative numbers, find a path from top left to bottom right 
# which minimizes the sum of all numbers along its path.


class Solution(object):
    # 44 ms, 36.81%
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])

        dp = grid
        
        for i in range(1, col):
            dp[0][i] += dp[0][i-1]
        for i in range(1, row):
            dp[i][0] += dp[i-1][0]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                
        return dp[-1][-1]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution().minPathSum(grid))