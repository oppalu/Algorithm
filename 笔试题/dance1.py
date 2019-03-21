# 1,4,16,64 4种硬币，1024的纸币。
# 用1024的纸币买了价值为N的商品，最少会收到多少硬币？

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    
    remain = 1024-n

    ans = 0
    ans += remain // 64
    remain = remain % 64
    ans += remain // 16
    remain = remain % 16
    ans += remain // 4
    remain = remain % 4
    ans += remain
    print(ans)
