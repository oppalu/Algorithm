# 快速排序的核心思想是使用元素的值对数组进行划分。实现其非递归方案。
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100

# 返回基准下标
def partition(arr, low, high):
    pivot = arr[low]

    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]

        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]

    arr[low] = pivot
    return low

# 将需要继续排序的首尾下标存入栈中，不断弹栈进行分区操作
def quicksort(arr):
    stack = []
    low = 0
    high = len(arr)-1
    stack.append(high)
    stack.append(low)

    while len(stack) > 0:
        low = stack.pop()
        high = stack.pop()
        pivot = partition(arr, low, high)

        if low < pivot - 1:
            stack.append(pivot-1)
            stack.append(low)
        if high > pivot + 1:
            stack.append(high)
            stack.append(pivot+1)

def solution():
    data = []
    while True:
        try:
            row = list(map(int, input().split(' ')))
            data.append(row[1:])
        except Exception:
            break

    for arr in data:
        quicksort(arr)
        print(" ".join(str(k) for k in arr))

solution()