# 求数据流中的中位数：如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
# 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

class Solution:
    def __init__(self):
        self.data = []

    def Insert(self, num):
        self.data.append(num)
        self.data = sorted(self.data)

    def GetMedian(self):
        if len(self.data) == 0:
            return None
        
        index = int(len(self.data)/2)

        if len(self.data) % 2 == 1:
            return self.data[index]
        else:
            return (self.data[index-1]+self.data[index])/2

s = Solution()
data = [5,2,3,4,1,6,7,0,8]
for i in data:
    s.Insert(i)
    print(s.GetMedian())