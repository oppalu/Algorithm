# 整数中1出现的次数
# 输入一个整数n，求从1到n整数的十进制表示中1出现的次数

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # 自己的解法，O(n*logn)
        if n < 1:
            return 0

        result = 0
        for i in range(1, n+1):
            temp=i
            while temp > 0:
                if temp % 10 == 1:
                    result += 1
                temp = int(temp/10)
        return result

    def NumberOf1Between1AndN_Solution2(self, n):
        # https://blog.csdn.net/yi_afly/article/details/52012593
        # O(logn)，分析见pad笔记
        if n < 1:
            return 0
            
        count = 0
        base = 1
        round = n
        while round > 0:
            weight = round % 10
            round = int(round / 10)
            count += round*base
            if weight == 1:
                # =1的时候，加上下一位的个数+1
                count += (n%base)+1
            elif weight > 1:
                # 大于1的时候，表明这一轮走完了，加上所在位数*10
                count += base
            base *= 10

        return count

print(Solution().NumberOf1Between1AndN_Solution2(12))