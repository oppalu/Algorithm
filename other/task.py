# 18字节跳动校招——任务调度
# 现在有N个PM，在某个时间会想出一个 idea，每个 idea 有提出时间、所需时间和优先等级。
# 对于一个PM来说，最想实现的idea首先考虑优先等级高的，相同的情况下优先所需时间最小的，还相同的情况下选择最早想出的。
# 同时有M个程序员，每个程序员空闲的时候就会查看每个PM尚未执行并且最想完成的一个idea,然后从中挑选出所需时间最小的一个idea独立实现，如果所需时间相同则选择PM序号最小的。
# 直到完成了idea才会重复上述操作。如果有多个同时处于空闲状态的程序员，那么他们会依次进行查看idea的操作。求每个idea实现的时间。

# 2 2 5(N、M、P)
# 1 1 1 2(PM序号、提出时间、优先等级和所需时间。)
# 1 2 1 1
# 1 3 2 2
# 2 1 1 2
# 2 3 5 5
# 3
# 4
# 5
# 3
# 9

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