# 构建乘积数组（不能使用除法）
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。

class Solution:
    def multiply(self, A):
        # write code here
        if not A or len(A)==0:
            return A
        B = [1] * len(A)
        temp = 1
        for i in range(len(A)):
            B[i] = temp
            temp *= A[i]

        temp = 1
        i = len(A)-1
        while i >= 0:
            B[i] *= temp
            temp *= A[i]
            i -= 1

        return B

arr = [1,2,3,4,5]
Solution().multiply(arr)