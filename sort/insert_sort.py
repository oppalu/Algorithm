# 插入排序
# 输入的每一行代表一个数组，其中的值用空格隔开，第一个值表示数组的长度。
# input:13 24 3 56 34 3 78 12 29 49 84 51 9 100

def solution():
    data = []
    while True:
        try:
            row = list(map(int, input().split(' ')))
            data.append(row[1:])
        except Exception:
            break

    for arr in data:
        for i in range(1,len(arr)):
            temp = arr[i]
            j = i-1
            while j >= 0 and arr[j] > temp:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
        print(" ".join(str(k) for k in arr))
solution()
