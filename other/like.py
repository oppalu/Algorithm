# 牛客网字节跳动算法——用户喜好

def Solution():
    n = int(input())
    likes = list(map(int, input().split()))

    data = {}
    for i in range(n):
        if likes[i] in data:
            data[likes[i]].append(i+1)
        else:
            data[likes[i]] = [i+1]

    q = int(input())

    for _ in range(q):
        temp = list(map(int, input().split()))
        l,r,k = temp[0], temp[1], temp[2]
        res = 0
        if k not in data:
            print(res)
        else:
            arr = data[k]

            for i in arr:
                if i>=l and i<=r:
                    res += 1
            print(res)

Solution()