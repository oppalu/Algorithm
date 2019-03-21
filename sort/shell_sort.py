# 实现Shell排序：设待排序元素序列有n个元素，首先取一个整数increment作为间隔将全部元素分为increment个子序列，所有距离为increment的元素放在同一个子序列中，在每一个子序列中分别实行直接插入排序。
# 然后缩小间隔increment，重复上述子序列划分和排序工作。直到最后取increment=1，将所有元素放在同一个子序列中排序为止。
# ex:8 9 1 7 2 3 5 4 6 0, gap=5，则变成3 5 1 6 0 8 9 4 7 2

# 输入第一行表示TC数，后面每个用例有两行，第一行为给定数组，第二行为指定间隔，每个间隔用空格隔开。输出的每一行为一个用例对应的指定排序结果。
# ex:
# 1
# 49 38 65 97 76 13 27 49 55 4
# 5 3
# output:13 4 49 38 27 49 55 65 97 76

def shell_sort(arr, increment):
    for i in range(increment, len(arr)):
        # 从间隔开始，对每一组大小进行比较交换
        while i >= increment and arr[i] < arr[i-increment]:
            arr[i], arr[i-increment] = arr[i-increment], arr[i]
            i -= increment
    return arr

def solution():
    num = int(input())

    for _ in range(num):
        data = list(map(int, input().split(' ')))
        increments = list(map(int, input().split(' ')))

        for incre in increments:
            shell_sort(data, incre)
        print(" ".join(str(i) for i in data))

solution()