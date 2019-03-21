# Given a collection of distinct integers, return all possible permutations.

class Solution:
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def perm(self, nums, i):
        if i == len(nums):
            self.res.append(nums.copy())
        for j in range(i, len(nums)):
            self.swap(nums, i, j)
            self.perm(nums, i+1)
            self.swap(nums, i, j)
    def permute(self, nums):
        #  68 ms, 21.30%
        self.res = []

        if not nums:
            return self.res

        self.perm(nums, 0)

        return self.res
    

arr = [1,2,3]
print(Solution().permute(arr))
