# 有一个由很多木棒构成的集合，每个木棒有对应的长度，请问能否用集合中的这些木棒以某个顺序首尾相连构成一个面积大于0的简单多边形且所有木棒都要用上
# 初始集合是空的，有两种操作，要么给集合添加一个长度为 L 的木棒，要么删去集合中已经有的某个木棒。
# 每次操作结束后你都需要告知是否能用集合中的这些木棒构成一个简单多边形。

# 5
# 1 1(操作类型，长度)
# 1 1
# 1 1
# 2 1
# 1 2

# No
# No
# Yes
# No
# No

def judge(data):
    if not data or len(data) <= 2:
        return 'No'
    max_v = max(data)
    other = sum(data)-max_v
    if max_v < other:
        return 'Yes'
    else:
        return 'No'

def Solution():

    nums = int(input())
    data = []
    for _ in range(nums):
        temp = list(map(int, input().split()))
        t, l = temp[0], temp[1]
        if t == 1:
            data.append(l)
        else:
            data.remove(l)
        
        print(judge(data))

Solution()