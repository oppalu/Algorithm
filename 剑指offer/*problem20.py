# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        if len(matrix) == 0:
            return res

        x_min = 0
        x_max = len(matrix)
        y_min = 0
        y_max = len(matrix[0])

        while x_min != x_max and y_min != y_max:
            i = x_min
            x_min += 1
            j = y_min

            while j < y_max:
                res.append(matrix[i][j])
                j += 1
            j-=1
            y_max -= 1

            i += 1
            while i < x_max:
                res.append(matrix[i][j])
                i += 1
            i-=1
            x_max -= 1

            j -= 1
            while j >= y_min:
                res.append(matrix[i][j])
                j -= 1
            j += 1
            y_min += 1

            i -= 1
            while i >= x_min:
                res.append(matrix[i][j])
                i -= 1
            i += 1

        return res

    def printMatrix2(self, matrix):
        # 思路：每次pop第一行，然后对剩下的数组进行逆时针翻转
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result


    def turn(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        res = []
        for i in range(col):
            temp = []
            for j in range(row):
                temp.append(matrix[j][i])
            res.append(temp)
        res.reverse()

        return res

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]

print(Solution().printMatrix2(matrix))
