# 1-n共n个楼，i楼高为i
# 有多少种排列满足从左到右能看到L种颜色（L-1次颜色的变化），答案对10^9+9取模。
# 能看到一个楼的前提是这个楼之前的楼都比它矮

# 4 3(n,L)
# 1 1 2 1(颜色)
# output=6

# 8 5
# 1 2 2 3 3 3 1 4
# output=432

import sys
num = 1000000009
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)


