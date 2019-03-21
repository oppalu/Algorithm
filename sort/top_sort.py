# 给定有向无环图中所有边，计算图的拓扑排序解的个数。
# 输入第一行为用例个数，后面每一行表示一个图中的所有边，边的起点和终点用空格隔开，边之间使用逗号隔开。
# (每次找入度为0的)
# 1
# a c,b c,c d,d e,d f,e g,f g
# output=4
# a b,a c,b c,b d,c d,c e,d e

def in_degree(nodes, names):
    degrees = dict((i, 0) for i in names)
    for v in nodes.values():
        for i in v:
            degrees[i] += 1

    res = []
    for i in degrees:
        if degrees[i] == 0:
            res.append(i)
    return res

def top_sort(nodes, name):
    if not nodes or not name:
        return 1

    next_list = in_degree(nodes, name)
    if not next_list:
        return 0
    
    result = 0
    for node in next_list:
        new_name = name.copy()
        new_name.remove(node)
        new_node = nodes.copy()
        new_node.pop(node)
        result += top_sort(new_node, new_name)
    return result

def Solution():
    nums = int(input())

    for _ in range(nums):
        temp = input().split(',')
        nodes = {}
        names = []
        for i in temp:
            node = i.split()
            if node[0] in nodes:
                nodes[node[0]].append(node[1])
            else:
                nodes[node[0]] = [node[1]]
            names.append(node[0])
            names.append(node[1])

        names = set(names)
        res = top_sort(nodes, names)
        print(res)

Solution()