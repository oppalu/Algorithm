# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

import itertools

class Solution:
    def Permutation(self, ss):
        # write code here
        res = []

        if not ss or len(ss)==0:
            return res
 
        def swap(arr, i,k):
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp
             
        def perm(arr, k):
            if k==len(arr):
                res.append(''.join(arr))
                return
            for i in range(k, len(arr)):
                swap(arr, i, k)
                perm(arr, k+1)
                swap(arr, i, k)
 
        arr = []
        for i in ss:
            arr.append(i)
        perm(arr, 0)
        return sorted(set(res))


    def Permutation2(self, ss):
        # write code here
        res = []

        if not ss or len(ss)==0:
            return res

        def perm(s, path):
            if len(s) == 0:
                res.append(path)
            else:
                for i in range(len(s)):
                    perm(s[:i]+s[i+1:], path+s[i])

        arr = []
        for i in ss:
            arr.append(i)
        perm(arr, '')
        return sorted(set(res))

s='abca'
print(Solution().Permutation(s))
