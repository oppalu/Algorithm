# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变 

class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for i in array:
            if i % 2 == 1:
                odd.append(i)
            else:
                even.append(i)
        return odd+even

    def reOrderArray2(self, array):
        # write code here
        for i in range(len(array)):
            if array[i] % 2 == 0:
                for j in range(i+1, len(array)):
                    if array[j] % 2 == 1:
                        array[i], array[j] = array[j], array[i]
                        break
        return array

res = Solution().reOrderArray([1,2,3,4,5,6])
print(res)