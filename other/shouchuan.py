# 牛客网字节跳动算法——手串
# 作为一个手串艺人，有金主向你订购了一条包含n个杂色串珠的手串——每个串珠要么无色，要么涂了若干种颜色。
# 为了使手串的色彩看起来不那么单调，金主要求，手串上的任意一种颜色（不包含无色），在任意连续的m个串珠里至多出现一次（注意这里手串是一个环形）。
# 手串上的颜色一共有c种。现在按顺时针序告诉你n个串珠的手串上，每个串珠用所包含的颜色分别有哪些。
# 请你判断该手串上有多少种颜色不符合要求。即询问有多少种颜色在任意连续m个串珠中出现了至少两次。

# 5 2 3(n，m，c)
# 3 1 2 3(第i颗有多少种颜色，分别是什么)
# 0
# 2 2 3
# 1 2
# 1 3

def Solution():
    temp = list(map(int, input().split()))
    n,m,c = temp[0],temp[1],temp[2]

    data = {}
    for i in range(n):
        temp = list(map(int, input().split()))
        if temp[0] != 0:
            for j in range(1, len(temp)):
                if temp[j] in data:
                    data[temp[j]].append(i)
                else:
                    data[temp[j]] = [i]

    res = 0
    print(data)
    for i in data:
        data[i] = sorted(data[i])
        for j in range(len(data[i])-1):
            if data[i][j+1]-data[i][j] <= m:
                res += 1
                break
    print(res)

Solution()