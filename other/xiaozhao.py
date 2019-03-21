# 牛客网2017校招题目——头条校招
# 一场考试包含3道开放性题目，假设他们的难度从小到大分别为a,b,c，我们希望这3道题能满足下列条件：
# a<=b<=c, b-a<=10, c-b<=10
# 现有n道题要分布到若干场考试中，计算最少还需要再出几道题

# 4  
# 20 35 23 40
# output = 2


def solution():
    n = int(input())
    data = list(map(int, input().split()))

    data = sorted(data)
    temp = 0
    for i in range(n-1):
        if data[i+1] - data[i] > 10:
            temp += 1

    if (temp+n) % 3 != 0:
        temp += 3 - (temp+n) % 3

    print(temp)

solution()
