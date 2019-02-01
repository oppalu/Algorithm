# 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 给出的所有元素都大于0，若数组大小为0，请返回0。

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        
        low = 0
        high = len(rotateArray)-1

        while low < high:
            mid = int((low+high)/2)
            if rotateArray[mid] > rotateArray[high]:
                low = mid +1
            elif rotateArray[mid] == rotateArray[high]:
                high = high -1
            else:
                high = mid

        return rotateArray[low]
        
arr = [3,4,5,1,2]
res = Solution().minNumberInRotateArray(arr)
print(res)