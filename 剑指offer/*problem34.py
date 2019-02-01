# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

import sys
class Solution:
    def GetUglyNumber_Solution1(self, index):
        #一般解法：写求丑数的算法，遍历对每个数进行判断
        def judge(N):
            while N % 2 == 0:
                N = N/2
            while N % 3 == 0:
                N = N/3
            while N % 5 == 0:
                N = N/5
            return True if N==1 else False

        if index < 1:
            return 0
        
        current = 0
        count = 0
        while count < index:
            current += 1
            if judge(current):
                count += 1
        return current

    def GetUglyNumber_Solution2(self, index):
        # 丑数应该是另一个丑数乘以2、3或者5的结果（1除外）。可以创建一个数组存放排好序的丑数，每个丑数是前面的丑数乘以2、3或者5得到的。
        # 用数组的3个值记录当前计算到哪个数的倍数了[如当前用了第2个丑数的*3结果，则表示3下标+1表示下次用第3个丑数的*3]，然后每次找*2,*3,*5里最小的结果
        if index < 1:
            return 0

        res = [1]
        index_2 = index_3 = index_5 = 0

        while len(res) < index:
            multi_2 = 2 * res[index_2]
            multi_3 = 3 * res[index_3]
            multi_5 = 5 * res[index_5]
            data = min(multi_2, multi_3, multi_5)
            res.append(data)

            if data == multi_2:
                index_2 += 1
            if data == multi_3:
                index_3 += 1
            if data == multi_5:
                index_5 += 1
            
        return res[-1]

print(Solution().GetUglyNumber_Solution2(12))