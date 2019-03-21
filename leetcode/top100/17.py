# letter combination of phone number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# (1:[],2:[abc], 3:[def], 4:[ghi], 5:[jkl], 6:[mno], 7:[pqrs], 8:[tuv], 9:[wxyz])

class Solution:
    def __init__(self):
        self.data = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        # 52ms, 19.00%
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [i for i in self.data[digits[0]]]
        
        start = self.data[digits[0]]
        return [i+j for i in start for j in self.letterCombinations(digits[1:])]

print(Solution().letterCombinations("23"))