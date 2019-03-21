# 找到给定数组的给定区间内的倒数第K小的数值（找最小的k个中最大的）
# 1. 用k个建最大堆
# 2. 剩下的中和最大的a[0]比，大的话pass否则替换重新建堆
# 3. 对剩下的k个最小的再排序，找最大的

from sys import stdin


def perc_down(array, start, end):
    root = array[start]
    son = 2 * start + 1

    while son < end:
        if son + 1 < end and array[son + 1] > array[son]:  # find the biggest son
            son += 1
        if root > array[son]:
            break
        else:
            # if parent is smaller than the biggest son, then replace it with the biggest son
            array[start] = array[son]
            start = son
            son = 2 * son + 1  # recurse
    array[start] = root


def build_heap(array):
    start = int(len(array) / 2)
    while start >= 0:
        perc_down(array, start, len(array))
        start -= 1


def find_k():
    input_array = stdin.readline().split(' ')

    index = stdin.readline().split(' ')
    index = [int(i) for i in index]

    input_array = input_array[index[0] - 1:index[1]]

    k = int(stdin.readline().strip())

    k_array = input_array[0:k]
    build_heap(k_array)

    for node in input_array[k:]:
        if node < k_array[0]:
            k_array[0] = node
            build_heap(k_array)

    index = len(k_array) - 1
    while index >= 0:
        k_array[0], k_array[index] = k_array[index], k_array[0]
        perc_down(k_array, 0, index)
        index -= 1
    print(k_array[k - 1])


find_k()