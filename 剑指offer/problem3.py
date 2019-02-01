# 二维数组的查找
# 一个二维数组从左到右，从上到下递增。完成函数，当输入一个二维数组和整数，判断数组中是否含有该整数

def solution(arr, n):
    row = len(arr)
    col = len(arr[0])

    # 从右上开始
    i = 0
    j = col-1

    while i < row and j >= 0:
        if arr[i][j] > n:
            j -= 1
        elif arr[i][j] < n:
            i += 1
        else:
            return True

    return False


arr = []
arr.append([1,2,8,9])
arr.append([2,4,9,12])
arr.append([4,7,10,13])
arr.append([6,8,11,15])

n = 5

print(solution(arr, n))


    
