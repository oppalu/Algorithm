# 按照给定的起始顶点深度优先遍历给定的无向图，尝试所有可能的遍历方式，打印遍历过程中出现的最大深度。
# 用例的第一行是图中节点的个数n和起始点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
# 1
# 4 a
# a b c d
# a 0 1 1 0
# b 1 0 1 0
# c 1 1 0 1
# d 0 0 1 0

path = set()
max_depth = -1

def dfs(graph, start, depth):
    global path
    global max_depth
    
    if depth > max_depth:
        max_depth = depth

    for node in graph[start]:
        if node not in path:
            path.add(node)
            dfs(graph, node, depth+1)
            path.remove(node)

def Solution():
    nums = int(input())

    for _ in range(nums):
        n, start = input().split()
        name = input().split()
        
        path.add(start)

        datas = {}
        for _ in range(int(n)):
            data = input().split()
            temp = list(map(int, data[1:]))
            nodes = []
            for i in range(int(n)):
                if temp[i] == 1:
                    nodes.append(name[i])
            datas[data[0]] = nodes

        dfs(datas, start, 1)
        print(max_depth)

Solution()
