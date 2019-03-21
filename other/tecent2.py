# 把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。

# AkleBiCeilD->kleieilABCD


def solution():
    try:
        while True:
            s = list(input())
            l = 0 # 大写字母个数
            for i in range(len(s)-1, -1, -1):
                if s[i] >= 'A' and s[i] <= 'Z':
                    temp = s[i]
                    for j in range(i+1, len(s)-l):
                        s[j-1] = s[j]
                    s[len(s)-l-1] = temp
                    l += 1

            print(''.join(s))

    except EOFError:
        pass

solution()