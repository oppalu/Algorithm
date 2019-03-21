# n个人排成一圈
# 1. 每个人至少一个奖品
# 2. 如果某个人分数比左右的高，则奖品数量要比左右的高
# 最少要准备多少个奖品？

# 2(测试用例)
# 2(n, 人数)
# 1 2(分数) ->3
# 4
# 1 2 3 3 ->8
# 3 4 1 2 -> 10

import sys
if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        values = list(map(int, sys.stdin.readline().split()))
        res = [1 for _ in range(n)]

        ans = 0
        while sum(res) != ans:
            ans = sum(res)
            for i in range(n):
                pre = (i-1+n) % n
                nex = (i+1+n) % n
                if values[i] > values[pre]:
                    res[i] = max(res[i], res[pre]+1)
                if values[i] > values[nex]:
                    res[i] = max(res[i], res[nex]+1)
        print(sum(res))