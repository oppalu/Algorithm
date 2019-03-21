# m种颜色气球，打了n枪。打爆所有颜色气球最少用了连续几枪

# 12 5
# 2 5 3 1 3 2 4 5 0 5 4 3
# output = 6

import sys
if __name__ == "__main__":
    values = list(map(int, sys.stdin.readline().strip().split()))
    n, m = values[0], values[1]

    data = list(map(int, sys.stdin.readline().strip().split()))
    
    if len(set(data)) < m or (len(set(data)) == m and 0 in set(data)):
        print(-1)
    else:
        ans = sys.maxsize
        for index in range(0, n-m+1):
            # 从每个开始暴力
            temp = data[index:]
            help_s = set()

            i = 0
            while i < len(temp):
                if temp[i] not in help_s and temp[i] != 0:
                    help_s.add(temp[i])
                if len(help_s) == m:
                    break
                i += 1
            if i != len(temp):
                j = 0
                while j < i+1:
                    if temp[j] not in temp[j+1:i+1]:
                        break
                    j += 1
                ans = min(ans, i-j+1)
        print(ans)
                


