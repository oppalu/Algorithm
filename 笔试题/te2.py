# 本题为考试多行输入输出规范示例，无需提交，不计分。

# 求数列的和，i个数字为i*(-1)^i。
# 给出区间求和
# 4
# 2 4(3)
# 2 2(2)
# 3 3(-3)
# 1 5(-3)


import sys
if __name__ == "__main__":
    q = int(sys.stdin.readline().strip())

    data = []
    for i in range(q):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        data.append(values)

    res = []
    for i in range(q):
        l_even = r_even = False
        if data[i][0] % 2 == 0:
            l_even = True
        if data[i][1] % 2 == 0:
            r_even = True

        if l_even and r_even:
            ans = data[i][1] - (data[i][1]-data[i][0])//2
            res.append(ans)
        elif not l_even and not r_even:
            ans = (data[i][1]-data[i][0])//2 - data[i][1]
            res.append(ans)
        elif not l_even and r_even:
            res.append((data[i][1]-data[i][0]+1)//2)
        else:
            res.append(-(data[i][1]-data[i][0]+1)//2)
    
    for i in res:
        print(str(i))


