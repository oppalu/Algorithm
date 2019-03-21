# counting bits
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num 
# calculate the number of 1's in their binary representation and return them as an array.

class Solution:
    def countBits(self, num):
        res = [0 for i in range(num+1)]

        for i in range(1, num+1):
            res[i] = res[i & (i-1)]+1

        return res


print(Solution().countBits(2))
print(Solution().countBits(5))