# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。如果不存在则输出0
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2

from collections import Counter
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # 个人解法，用字典存储每个数字出现次数，然后根据次数判断。O(n)
        if len(numbers) == 0:
            return 0
        count = Counter(numbers)
        data = count.most_common()[0]

        if data[1] > int(len(numbers)/2):
            return data[0]
        else:
            return 0


    def MoreThanHalfNum_Solution2(self, numbers):
        # 书上解法，摩尔投票法：每次从数组中找出一对不同的元素，将其从数组中删除。如果最后数组为空，则没有任何元素出现的次数超过该数组长度的一半
        # 假设有这个数字，那么它的数量一定比其它所有数字之和还要多
        # 在遍历数组时保存两个值：一是数组中一个数字，一是次数。遍历下一个数字时，若它与之前保存的数字相同，则次数加1，否则次数减1；
        # 若次数为0，则保存下一个数字，并将次数置为1。遍历结束后，所保存的数字即为所求。然后再判断它是否符合条件即可。
        if not numbers:
            return 0
        num = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if count == 0:
                num = numbers[i]
                count = 1
            elif numbers[i] == num:
                count += 1
            else:
                count -= 1
    
        count = 0
        for i in numbers:
            if i == num:
                count += 1
        return num if count > len(numbers) / 2.0 else 0

    

arr = [1,2,3,2,2,2,5,2,4]
print(Solution().MoreThanHalfNum_Solution(arr))