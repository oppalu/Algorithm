# happy number
# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.


class Solution:
    def isHappy(self, n):
        # time limited
        if not n:
            return False
        dicts = set()
        while True:
            bits = list(map(int, list(str(n))))
            n = sum(i**2 for i in bits)
            if n == 1:
                return True
            if n in dicts:
                return False
            else:
                dicts.add(n)
        return False



print(Solution().isHappy(2))