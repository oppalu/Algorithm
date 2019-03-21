# 18字节跳动校招——水仙花数
# “水仙花数”是指一个三位数，它的各位数字的立方和等于其本身，比如：153=1^3+5^3+3^3。 现在要求输出所有在[m,n]范围内的水仙花数。

# 100 120(no)
# 300 380(370 371)

def isFlower(n):
    temp = n
    ans = 0
    while temp:
        ans += pow(temp%10,3)
        temp //= 10
    return True if ans == n else False

def Solution():
    while True:
        try:
            data = list(map(int, input().split(' ')))
            m,n = data[0], data[1]

            res = []
            for i in range(m, n+1):
                if isFlower(i):
                    res.append(i)
            
            if len(res) == 0:
                print("no")
            else:
                print(" ".join(str(i) for i in res))
        except Exception:
            break

Solution()