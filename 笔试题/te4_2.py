# m种颜色气球，打了n枪。打爆所有颜色气球最少用了连续几枪

# 12 5
# 2 5 3 1 3 2 4 1 0 5 4 3
# 2 5 3 1 3 2 4 1 2 5 4 3
# 2 5 3 1 3 2 4 5 0 5 4 3
# output = 6

# 把气球序列逐个放入队列当中，并记录当前队列中每种颜色出现的次数，并维护当前队列中颜色的总数。当队首的气球颜色数量大于1的时候，就应该出队。当队列中颜色的总数为m的时候，我们就更新答案为队列的长度，整个过程更新出的最大值即为答案。


import sys
if __name__ == "__main__":
    values = list(map(int, sys.stdin.readline().strip().split()))
    n, m = values[0], values[1]

    data = list(map(int, sys.stdin.readline().strip().split()))

    ans = sys.maxsize
    queue = []
    cnt = [0 for _ in range(m)]

    for i in data:
        queue.append(i)
        if i != 0:
            cnt[i-1] += 1
        while cnt[queue[0]-1] > 1 or queue[0] == 0:
            if queue[0] != 0:
                cnt[queue[0]-1] -= 1
            queue = queue[1:]
        col = 0
        for i in cnt:
            if i != 0:
                col += 1
        if col == m:
            ans = min(ans, len(queue))
    print(ans)

