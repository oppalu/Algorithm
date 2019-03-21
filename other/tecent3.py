# 有n个数，两两组成二元组，相差最小的有多少对呢？相差最大呢？
# 6
# 45 12 45 32 5 6
# output=1 2

# 差最大：最大值个数*最小值个数
# 差最小：有重复值为重复值，否则相邻相减

import sys
def solution():
    try:
        while True:
            n = int(input())
            data = list(map(int, input().split()))
            data = sorted(data)
            
            counter = {}
            for i in data:
                if i in counter:
                    counter[i] += 1
                else:
                    counter[i] = 1

            max_v = counter[data[-1]] * counter[data[0]]
            min_v = 0
            if len(counter) == len(data):
                temp = sys.maxsize
                for i in range(len(data)-1):
                    if data[i+1] - data[i] <= temp:
                        temp = data[i+1] - data[i]
                        min_v += 1
            else:
                # 有重复值
                for i in counter:
                    if counter[i] != 1:
                        min_v += (counter[i]-1)
            print(min_v, max_v)

    except EOFError:
        pass

solution()