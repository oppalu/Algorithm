# 本题为考试多行输入输出规范示例，无需提交，不计分。

# 货币：货币面额1-n, 每种货币无限多。
# 输入n, m，求最少的硬币数(n为最大货币面值，m为商品价格)
# 6 7
# 2

import sys
if __name__ == "__main__":
    # for line in sys.stdin:
    #     a = line.split()
    #     print(int(a[0]), int(a[1]))

    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    n, m = values[0], values[1]

    res = 0

    while m > 0:
        res += 1
        if m >= n:
            m -= n
        else:
            break
    print(res)