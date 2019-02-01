# 输入n个整数，找出其中最小的K个数。

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 堆：先放k个，然后建最大堆，每次与0即最大的比，大于就pass，小于就替换然后重新建堆。最后对最小的k个排序
        if k <= 0 or len(tinput)<k or len(tinput)==0:
            return []

        k_array = tinput[0:k]
        self.build_heap(k_array)
        for i in tinput[k:]:
            if i < k_array[0]:
                k_array[0] = i
                self.build_heap(k_array)
        
        return sorted(k_array)

    def build_heap(self, array):
        start = int(len(array)/2)
        while start >= 0:
            self.perc_down(array, start, len(array))
            start -= 1

    def perc_down(self, array, start, end):
        root = array[start]
        son = 2 * start + 1

        while son < end:
            if son + 1 < end and array[son+1] > array[son]:
                son += 1
            if root > array[son]:
                break
            else:
                array[start] = array[son]
                start = son
                son = 2 * son + 1
        array[start] = root



arr = [4,5,1,6,2,7,3,8]
print(Solution().GetLeastNumbers_Solution(arr, 0))
