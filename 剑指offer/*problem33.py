# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。


class Solution:
    def PrintMinNumber(self, numbers):
        # 拼接两个字符串，比较mn与nm大小
        if not numbers or len(numbers)==0:
            return ""

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                a = int(str(numbers[i])+str(numbers[j]))
                b = int(str(numbers[j])+str(numbers[i]))
                if a > b:
                    temp = numbers[j]
                    numbers[j] = numbers[i]
                    numbers[i] = temp
        
        return "".join(str(i) for i in numbers)

arr = [3,32,321]
print(Solution().PrintMinNumber(arr))