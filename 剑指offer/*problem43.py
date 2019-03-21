# n个骰子的点数：有n个骰子，所有骰子朝上点数之和为s，打印出s所有可能的值出现的概率
# 求所有值出现的次数，然后除以总数求概率
# 动态规划： f(n,Sum) = f(n-1,Sum-1) + f(n-1,Sum-2) + f(n-1,Sum-3) + f(n-1,Sum-4) + f(n-1,Sum-5) + f(n-1,Sum-6) 

class Solution:
    def dicesSum(self, n):
        if n < 1:
            return
        # 利用一个辅助数组，第i行表示第i+1个骰子每种可能的和的值会出现的次数
        value = [[0 for i in range(6*n)] for i in range(n)]
        # 初始化第一行，第一个骰子可能出现的和为1-6，可能出现的次数为1
        for i in range(6):
            value[0][i] = 1

        for i in range(1,n):
            # 第i行的和范围在[i, 6*(i+1)]之间，如第1行表示2个骰子，和在[6,12]之间
            for j in range(i,6*(i+1)):
                value[i][j] = value[i-1][j-1]+value[i-1][j-2]+value[i-1][j-3]+value[i-1][j-4]+value[i-1][j-5]+value[i-1][j-6]
        
        count = value[n-1]
        total = 6**n
        res = []
        for i in range(n-1, len(count)):
            temp = [i+1, count[i]/total]
            res.append(temp)
        return res
print(Solution().dicesSum(1))