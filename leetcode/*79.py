# word search(类似剑指offer中矩阵搜索)
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if not word:
            return True
        rows = len(board)
        cols = len(board[0])

    def search():
        


board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]

print(Solution().exist(board, 'ABCCED'))
print(Solution().exist(board, 'SEE'))
print(Solution().exist(board, 'ABCB'))