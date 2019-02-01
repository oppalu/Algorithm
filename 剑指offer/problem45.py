# 约瑟夫环问题

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        arr = [i for i in range(n)]
        index = 0
        while len(arr) > 1:
            index += (m-1)
            index = index % len(arr)
            arr.remove(arr[index])

        return arr[0]

    def LastRemaining_Solution2(self, n, m):
        # 方法2，找递归公式。f(n,m)表示在n个数字中删掉第m个剩下的数字，
        # 则n=1时，f(n,m)=0。其余情况f(n,m)=[f(n-1,m)+m]%n
        if n < 1 or m < 1:
            return -1
        
        res = 0
        for i in range(2, n+1):
            res = (res+m) % i
        return res

Solution().LastRemaining_Solution(5,2)