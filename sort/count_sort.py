# 实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。
# 计数排序：
# 1)找A的最大值
# 2)新建B数组，长度为MAX+1
# 3)B中存元素出现次数(i放在下标为i的)
# 4)遍历B输出

def find_max(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

def solution():
    data = []
    while True:
        try:
            row = list(map(int, input().split(' ')))
            data.append(row[1:])
        except Exception:
            break

    for arr in data:
        max = find_max(arr)
        temp = []
        for i in range(max+1):
            temp.append(0)

        for i in range(len(arr)):
            temp[arr[i]] += 1

        result = []
        for i in range(len(temp)):
            times = temp[i]
            for j in range(times):
                result.append(i)

        print(" ".join(str(k) for k in result))
solution()