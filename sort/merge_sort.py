# 合并（归并）排序的核心思想是：每次从中间位置将数组分组再分别排序。请实现其非递归方案。
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100

# arr的[left, mid] [mid+1, right]是两个排好序的，要把两个合并成新数组返回
def merge(arr, left, mid, right):
    i = left
    j = mid+1

    result = []

    while i<=mid and j<=right:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    # 对于一方已经到结尾的情况
    if i <= mid:
        result.extend(arr[i:mid+1])
    if j <= right:
        result.extend(arr[j:right+1])

    return result


def merge_sort(arr, size):
    i = 0

    result = []
    while i+2*size <= len(arr):
        temp = merge(arr, i, i+size-1, i+2*size-1)
        result.extend(temp)
        i += 2*size
    
    # 未合并的元素个数大于 size,合并最后两个
    if i+size < len(arr):
        temp = merge(arr, i, i+size-1, len(arr)-1)
        result.extend(temp)
    # 否则直接加入
    else:
        result.extend(arr[i:])

    return result


def solution():
    data = []
    while True:
        try:
            row = list(map(int, input().split(' ')))
            data.append(row[1:])
        except Exception:
            break

    for arr in data:
        temp_arr = []
        size = 1
        while size < len(arr):
            temp_arr = merge_sort(arr, size)
            size *= 2
            arr = merge_sort(temp_arr, size)
            size *= 2
        print(" ".join(str(k) for k in arr))


solution()