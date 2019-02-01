# 统计一个数字在排序数组中出现的次数。

from collections import Counter
class Solution:
    def GetNumberOfK(self, data, k):
        # O(n)
        counter = Counter(data)
        return counter[k]

    def GetNumberOfK2(self, data, k):
        # 二分查找，找第一个k的位置和最后一个的位置
        def getFirstK(data, k, start, end):
            if start > end:
                return -1
            mid = int((start+end)/2)
            if data[mid] == k:
                if (mid > 0 and data[mid-1] != k) or mid == 0:
                    return mid
                else:
                    end = mid-1
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
            return getFirstK(data, k, start, end)

        def getLastK(data, k, start, end):
            if start > end:
                return -1
            mid = int((start+end)/2)
            if data[mid] == k:
                if (mid < len(data)-1 and data[mid+1] != k) or mid == len(data) -1:
                    return mid
                else:
                    start = mid+1
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
            return getLastK(data, k, start, end)
        
        if not data or len(data) == 0:
            return 0
        
        first = getFirstK(data, k ,0, len(data)-1)
        last = getLastK(data, k ,0, len(data)-1)

        if first == -1 or last == -1:
            return 0

        return last-first+1


arr = [1,2,3,3,3,3,4,5]

print(Solution().GetNumberOfK2(arr, 3))