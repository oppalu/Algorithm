# 给定 x, k ，求满足 x + y = x | y 的第 k 小的正整数 y 。 | 是二进制的或(or)运算，例如 3 | 5 = 7。
# 比如当 x=5，k=1时返回 2，因为5+1=6 不等于 5|1=5，而 5+2=7 等于 5 | 2 = 7。
# 5 1->2
def Solution():
    x, k = map(int, input().split())
    
    res = []
    i = 1

    while len(res) < k:
        if x + i == x | i:
            res.append(i)
        i += 1

    print(res[-1])

Solution()