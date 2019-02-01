# 数组中只出现一次的数字，要求时间复杂度O(n),空间复杂度O(1)
# 一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字

from collections import Counter
class Solution:
    def FindNumsAppearOnce(self, array):
        # 方法一，记录每个数字出现的次数
        counter = Counter(array)
        res = []
        for i in counter:
            if counter[i] == 1:
                res.append(i)
        return res

    def FindNumsAppearOnce2(self, array):
        # 方法2异或：所有数与0做异或，由于自己与自己异或=0，0与自己异或=自己。所以所有元素异或后的结果为2个只出现1次的数字异或的值
        # 然后找最后这个数字从右边起第一个为1的位(这说明这两个数一个在这一位=1另一个=0)，
        # 然后遍历数组将元素分为2组，一组这一位=0另一组=1，然后两组元素分别做异或剩下的就是两个数
        if not array:
            return []
        data = 0
        for i in array:
            data ^= i
     
        index = 0
        while data & 1 == 0:
            index += 1
            data >>=1

        a = b = 0
        for i in array:
            if self.isBit(i, index):
                a ^= i
            else:
                b ^= i
        return [a, b]
 
    def isBit(self, num, idx):
        #判断num的二进制从右边起idx位是不是1
        num >>= idx
        return num & 1

arr = [2,4,3,6,3,2,5,5]
print(Solution().FindNumsAppearOnce2(arr))