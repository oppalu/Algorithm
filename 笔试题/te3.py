# 本题为考试多行输入输出规范示例，无需提交，不计分。

# 石头剪刀布每人各选了n张，依次比对赢了+1
# 已知A的每张牌及B的得分，求B的排列方案有多少种

# 3 2(n, 得分s)
# 0 1 2（石头 布 剪刀）
# output=6
# 结果对10^9+7取模

# 问题：考虑边界s>n的情况

import sys
import math
num = 1000000007
def fac(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
if __name__ == "__main__":
    values = list(map(int, sys.stdin.readline().strip().split()))
    n, s = values[0], values[1]

    data = list(map(int, sys.stdin.readline().strip().split()))
    
    win_times = fac(n) // (fac(s)*fac(n-s))
    ans = win_times * (2 ** (n-s))
    print(ans % num)