# 自动校对程序
# 1. 三个相同的字母连在一起，去掉一个
# 2. 两对一样的字母(AABB)， 去掉第二对的第一个字母
# 3. 优先从左到右匹配：AABBCC ->先修复AABB

# 2
# helloo->hello
# wooooooow->woow

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        line = sys.stdin.readline().strip()
        s = [i for i in line]
        i = 0
        while i < len(s)-2:
            if s[i] == s[i+1]:
                if s[i] == s[i+2]:
                    s = s[0:i]+s[i+1:]
                else:
                    if i == len(s)-3:
                        break
                    if s[i+2] == s[i+3]:
                        s = s[0:i+2]+s[i+3:]
                    else:
                        i += 1
            else:
                i += 1
        print(''.join(i for i in s))



