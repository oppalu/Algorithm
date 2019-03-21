# subsets

# Given a set of distinct integers, nums, return all possible subsets (the power set).

class Solution:
    def subsets(self, nums):
        # 法1：循环。44 ms, 54.80% 
        res = [[]]
        for i in nums:
            res += [j+[i] for j in res]
        return res

    def subset2(self, nums):
        # 法2：DFS。44 ms, 54.80%
        res = []
        nums.sort()
        
        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])

        dfs(0, [])
        return res


print(Solution().subset2([1,2,3]))