# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        return self.VerifySquenceOfBST2(sequence)

    def VerifySquenceOfBST2(self, sequence):
        # write code here
        if len(sequence) == 0:
            return True
        
        root = sequence[-1]
        left = []
        right = []
        i = 0

        while sequence[i] < root:
            left.append(sequence[i])
            i += 1

        right = sequence[i:-1]

        for i in right:
            if i < root:
                return False
            
        return self.VerifySquenceOfBST2(left) and self.VerifySquenceOfBST2(right)


arr1 = [5,7,6,9,11,10,8]
print(Solution().VerifySquenceOfBST(arr1))
arr2 = [7,4,6,5]
print(Solution().VerifySquenceOfBST(arr2))
arr3 = []
print(Solution().VerifySquenceOfBST(arr3))