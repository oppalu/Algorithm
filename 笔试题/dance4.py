# n根绳子，i根长度为li, 需要m根等长的绳子，可以任意裁剪。求m根最长的长度

# 3 4(n, m)
# 3 5 4(l)
# output=2.50

import sys
if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    n, m = map(int, line.split())
    line = sys.stdin.readline().strip()
    data = list(map(int, line.split()))

    if m <= n:
        l.sort(reverse = True)
        print('%.2f' % data[m-1])
    else:
        max_l = sum(data)/m

        l, r = 0, max_l
        while l <= r:
            mid = l + (r-l)/2

            temp = 0
            for i in range(len(data)):
                temp += data[i]//mid
            if temp >= m:
                l = mid+0.001
            else:
                r = mid-0.001

        print('%.2f' % l)