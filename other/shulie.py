# 18字节跳动校招——数列的和
# 数列的定义如下：数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。（精度保留2位小数。）

from math import sqrt

def Solution():
    while True:
        try:
            data = list(map(int, input().split(' ')))
            n,m = data[0], data[1]
            res = 0
            for _ in range(m):
                res += n
                n = sqrt(n)
            print('%.2f' %res)
        except Exception:
            break

Solution()

