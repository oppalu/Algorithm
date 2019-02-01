# 设计一个函数判断一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
# 如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
# ex:
# a b c e 
# s f c s
# a d e e 
# 包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径


class Solution:
    # rows&cols分别是行数&列数，matrix也是字符串
    def hasPath(self, matrix, rows, cols, path):
        if not matrix:
            return False
        if not path:
            return True
        # 找到与path第一个元素相等的元素的下标，然后分别从这些下标开始逐个判断
        idx = [i for i in range(len(matrix)) if matrix[i] == path[0]]
        for i in idx:
            if self.findPath(matrix, rows, cols, path, i, []):
                return True
        return False
 
    def findPath(self, matrix, rows, cols, path, current, visited):
        if current in visited:
            return False
        if current < 0 or current >= len(matrix):
            return False
        if not path:
            return False
        if matrix[current] != path[0]:
            return False

        if len(path) == 1:
            return True
        
        visited.append(current)
        # 判断方位：
        # 第一个元素
        if current == 0:
            return self.findPath(matrix, rows, cols, path[1:], current+1, visited) or self.findPath(matrix, rows, cols, path[1:], current+cols, visited)
        # 最后一个元素
        if current == len(matrix)-1:
            return self.findPath(matrix, rows, cols, path[1:], current-1, visited) or self.findPath(matrix, rows, cols, path[1:], current-cols, visited)
        # 第一列
        if current % cols == 0:
            return self.findPath(matrix, rows, cols, path[1:], current-cols, visited) or self.findPath(matrix, rows, cols, path[1:], current+cols, visited)\
            or self.findPath(matrix, rows, cols, path[1:], current+1, visited)
        # 最后一列
        if (current+1) % cols == 0:
            return self.findPath(matrix, rows, cols, path[1:], current-cols, visited) or self.findPath(matrix, rows, cols, path[1:], current+cols, visited)\
            or self.findPath(matrix, rows, cols, path[1:], current-1, visited)
        # 其他
        else:
            return self.findPath(matrix, rows, cols, path[1:], current-cols, visited) or self.findPath(matrix, rows, cols, path[1:], current+cols, visited)\
            or self.findPath(matrix, rows, cols, path[1:], current+1, visited) or self.findPath(matrix, rows, cols, path[1:], current-1, visited)
 
# s = Solution()
# matrix = "ABCESFCSADEE"
# path = "ABCB"
# rows = 3
# cols = 4
# print s.hasPath(matrix, rows, cols, path)