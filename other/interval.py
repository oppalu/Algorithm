# 18字节跳动校招——选区间
# 给定一个数组序列,需要求选出一个区间,使得该区间是所有区间中经过（区间中的最小数*区间所有数的和）的值最大的一个：
# 如给定序列 [6 2 1]则根据上述公式,可得到所有可以选定各个区间的计算值:
# [6] = 6 * 6 = 36;
# [2] = 2 * 2 = 4;
# [1] = 1 * 1 = 1;
# [6,2] = 2 * 8 = 16;
# [2,1] = 1 * 3 = 3;
# [6, 2, 1] = 1 * 9 = 9;
# 从上述计算可见选定区间[6]，计算值为36， 则程序输出为36。
# 3(个数)
# 6 2 1
def Solution():
    nums = int(input())
    data = list(map(int, input().split(' ')))

    res = 0
    # 每个数作为最小值，找其为最小值的最大序列，求和相乘
    for i in range(len(data)):
        start = end = i
        while start-1 >= 0 and data[start-1] >= data[i]:
            start -= 1
        while end+1 <= len(data)-1 and data[end+1] >= data[i]:
            end += 1
        temp = data[i] * sum(data[start:end+1])
        res = max(res, temp)
    print(res)

Solution()