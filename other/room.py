# 字节跳动编程题2
# 有n个房间，现在i号房间里的人需要被重新分配，分配的规则是这样的：先让i号房间里的人全都出来，接下来按照 i+1, i+2, i+3, ... 的顺序依此往这些房间里放一个人，
# n号房间的的下一个房间是1号房间，直到所有的人都被重新分配。
# 现在告诉你分配完后每个房间的人数以及最后一个人被分配的房间号x，你需要求出分配前每个房间的人数。数据保证一定有解，若有多解输出任意一个解。

# 3 1(n房间数量, x最后一个人被分配的房间号)
# 6 5 1（每个房间分配后的人数）
# output：4 4 4（每个房间分配前的人数）

def Solution():
    temp = list(map(int, input().split()))
    n, x = temp[0], temp[1]-1
    after = list(map(int, input().split()))

    base = min(after)
    if after.count(base) == 1:
        i = after.index(base)
    else:
        j = x
        while True:
            if after[j] == base:
                i = j
                break
            j = (j-1) if j >= 1 else j+n-1
    # iteration为原i房间人数
    iterations = base*n
    if i == x:
        pass
    elif i > x:
        iterations += (n+x-i)
    else:
        iterations += (x-i)

    for j in range(n):
        if j == i:
            after[j] = iterations
        elif i == x:
            after[j] -= base
        elif i > x:
            if j > i or j <= x:
                after[j] -= (base+1)
            else:
                after[j] -= base
        else:
            if j > i and j <= x:
                after[j] -= (base+1)
            else:
                after[j] -= base

    print(after)
Solution()