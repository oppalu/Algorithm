# Sort Array By Parity II

# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.

class Solution:
    # 132 ms, faster than 87.77% 。空间复杂度less than 20.13%
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        res = []
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])

        return res

    # 132 ms, faster than 87.77%。空间复杂度less than 91.13% 
    def sortArrayByParityII2(self, A):
        # 方法2，直接交换：如果所在位置是正确的就到下一个位置，否则交换
        even = 0
        odd = 1

        while even<len(A) and odd<len(A):
            if A[even] % 2 == 0:
                even += 2
            elif A[odd] % 2 ==1:
                odd += 2
            else:
                A[even], A[odd] = A[odd], A[even]
                even += 2
                odd += 2

        return A

arr = [4,2,5,7]
print(Solution().sortArrayByParityII2(arr))