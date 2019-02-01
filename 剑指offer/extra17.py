# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

class Solution:

    def judge(self, threshold, i, j):
        sum1 = sum(map(int, list(str(i))))
        sum2 = sum(map(int, list(str(j))))
        return True if sum1+sum2 <= threshold else False

    def movingCount(self, threshold, rows, cols):
        # write code here
        def search(threshold, i, j):
            if not self.judge(threshold, i, j) or [i,j] in res:
                return

            res.append([i,j])
            if i+1 < rows:
                search(threshold, i+1, j)
            if j+1 < cols:
                search(threshold, i, j+1)

        res = []
        search(threshold, 0, 0)
        return len(res)

print(Solution().movingCount(7, 5,5))