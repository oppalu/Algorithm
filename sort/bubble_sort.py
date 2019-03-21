# 冒泡排序
# 输入的每一行代表一个数组，其中的值用空格隔开，第一个值表示数组的长度。

def solution():
    data = []
    while True:
        try:
            row = list(map(int, input().split(' ')))
            data.append(row[1:])
        except Exception:
            break

    for arr in data:
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        print(" ".join(str(k) for k in arr))
solution()