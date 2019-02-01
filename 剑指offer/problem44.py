# 从扑克牌中随机抽5张牌，判断是不是一个顺子(即是否连续,A=1,J=11,Q=12,K=13,大小王为任意数字)

class Solution:
    def IsContinuous(self, numbers):
        # 除0之外，max-min要小于剩下元素的长度，且不能有重复元素
        if not numbers or len(numbers) != 5:
            return False

        numbers = sorted(numbers)
        i = 0
        while numbers[i] == 0:
            i += 1
        if i > len(numbers):
            return False
        min_v = numbers[i]
        max_v = numbers[-1]

        if max_v-min_v > len(numbers)-1:
            return False

        for j in range(i, len(numbers)-1):
            if numbers[j] == numbers[j+1]:
                return False
        return True

arr = [0,3,2,6,4]
print(Solution().IsContinuous(arr))