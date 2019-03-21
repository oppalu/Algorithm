# Squares of a Sorted Array

# Given an array of integers A sorted in non-decreasing order, 
# return an array of the squares of each number, also in sorted non-decreasing order.

class Solution:
    # 144 ms, faster than 90.75% 
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        res = []

        for i in A:
            res.append(i*i)
        
        res = sorted(res)
        return res

    # 156 ms, faster than 70.74%
    def sortedSquares2(self, A):
        # 方法2，特性在于绝对值中间小两边大
        res = []
        l, r = 0, len(A)-1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                res.append(left*left)
                l += 1
            else:
                res.append(right*right)
                r -= 1
        res.reverse()
        return res

A1= [-4,-1,0,3,10]
A2 = [-7,-3,2,3,11]

res = Solution().sortedSquares2(A1)
print(res)