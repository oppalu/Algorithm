# 二分插入排序
# input:13 24 3 56 34 3 78 12 29 49 84 51 9 100

def binary_sort(data):
    for i in range(len(data)):
        left, right = 0, i-1
        temp = data[i]
        while left <= right:
            mid = (left+right)//2
            if temp < data[mid]:
                right = mid-1
            else:
                left = mid +1
        j = i-1
        while j >= left:
            data[j+1] = data[j]
            j -= 1
        if left != i:
            data[left] = temp
    return data

def solution():
    data = [13,24,3,56,34,3,78,12,29,49,84,51,9,100]

    for i in range(1,len(data)):
        data = binary_sort(data)
    print(data)
solution()