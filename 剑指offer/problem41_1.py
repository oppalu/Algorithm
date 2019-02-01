# 和为S的连续正数序列
# 输入一个正数s，输出所有和为S的连续正数序列(至少含2个数)。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
# ex:15, 输出1-5,4-6,7-8

class Solution:
    def FindContinuousSequence(self, tsum):
        # 思路同前，两个指针，初始时为0和1，然后求和，小了后面的指针+1，大了前面的指针+1
        if tsum == 1:
            return []
        data = [i for i in range(1, tsum)]
        begin = 0
        end = 1
        res = []

        while end < len(data):
            temp_sum = sum(data[begin:end+1])
            if temp_sum == tsum:
                res.append(data[begin:end+1])
                begin += 1
                end += 1
            elif temp_sum < tsum:
                end += 1
            else:
                begin += 1
        
        return res

print(Solution().FindContinuousSequence(15))