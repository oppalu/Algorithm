# 给出 n 个字符串，对于每个n个排列p，按排列给出的顺序(p[0] , p[1] … p[n-1])依次连接这 n 个字符串都能得到一个长度为这些字符串长度之和的字符串。
# 所以按照这个方法一共可以生成 n! 个字符串。
# 一个字符串的权值等于把这个字符串循环左移 i 次后得到的字符串仍和原字符串全等的数量，i 的取值为 [1 , 字符串长度]。
# 求这些字符串最后生成的 n! 个字符串中权值为 K 的有多少个。

# 3 2
# AB
# RAAB
# RA
# output=3
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def perm(arr, i, res):
    if i == len(arr):
        res.append(''.join(a for a in arr))
    for j in range(i, len(arr)):
        swap(arr, i, j)
        perm(arr, i+1, res)
        swap(arr, i, j)

def Solution():
    n, k = input().split()

    data = []
    for _ in range(int(n)):
        data.append(input())
    res = []
    perm(data, 0, res)

    ans = 0
    for s in res:
        temp = 0
        for i in range(1, len(s)+1):
            temp_s = s[i:]+s[0:i]
            if temp_s == s:
                temp += 1
        if temp == int(k):
            ans += 1
        
    print(ans)
Solution()