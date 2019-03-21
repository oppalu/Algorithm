# 按照给定的起始顶点广度优先遍历图，每一次通过字母顺序选择顶点查找下一层邻接点，打印遍历顺序。
# 用例第一行是节点个数n和开始顶点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。

# 1
# 4 a
# a b c d
# a 0 1 1 0
# b 1 0 1 0
# c 1 1 0 1
# d 0 0 1 0

# a b c d e
# a 0 1 1 0 1
# b 1 0 0 1 0
# c 1 0 0 0 1
# d 0 1 0 0 0
# e 1 0 1 0 0

def bfs(datas, start):
    queue = [start]
    res = [start]

    while queue:
        temp = []
        for i in queue:
            for j in datas[i]:
                if j not in res:
                    res.append(j)
                    temp.append(j)
        queue = temp
    return res


def Solution():
    nums = int(input())

    for _ in range(nums):
        n, start = input().split()
        name = input().split()

        datas = {}
        for _ in range(int(n)):
            data = input().split()
            temp = list(map(int, data[1:]))
            nodes = []
            for i in range(int(n)):
                if temp[i] == 1:
                    nodes.append(name[i])
            datas[data[0]] = nodes
        
        res = bfs(datas, start)
        print(" ".join(str(i) for i in res))

Solution()
