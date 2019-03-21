# 字节跳动2018校招——编程题1
# 定义点集P中某点x，如果x满足P中任意点都不在x的右上方区域内（横纵坐标都大于x），则称其为“最大的”。求出所有“最大的”点的集合。

# 5
# 1 2
# 5 3
# 4 6
# 7 5
# 9 0
# output:（按X轴从小到大的方式输出）
# 4 6
# 7 5
# 9 0

# 10
# 298498081 747278511
# 427131847 460128162
# 939984059 817455089
# 911902081 683024728
# 474941318 6933274
# 140954425 607811211
# 336122540 629431445
# 208240456 458323237
# 646203300 469339106
# 106410694 436340495

# 1. 暴力（先按x排序，则在i之后的都在i的下方）
def Solution():

    nums = int(input())

    data = []
    for _ in range(nums):
        data.append(list(map(int, input().split())))
    
    data = sorted(data)

    res = data.copy()
    i = 0
    while i < len(data):
        for j in range(i+1, len(data)):
            if data[j][1] > data[i][1]:
                res.remove(data[i])
                break
        i += 1

    res = sorted(res)
    result = map(lambda e: "{0} {1}".format(e[0], e[1]), res)
    print("\n".join(result))

# 2. 从最大的开始，用max_x max_y标记当前的最大值
def Solution2():

    nums = int(input())

    data = []
    for _ in range(nums):
        data.append(list(map(int, input().split())))
    
    data = sorted(data)
    data.reverse()

    res = []
    max_x = max_y = 0
    for i in data:
        if i[0] > max_x or i[1] > max_y:
            res.append(i)
            max_x = i[0]
            max_y = i[1]
    
    res = sorted(res)
    result = map(lambda e: "{0} {1}".format(e[0], e[1]), res)
    print("\n".join(result))
Solution2()