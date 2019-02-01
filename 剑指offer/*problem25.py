# (其他解法见leetcode113)
# 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        all_path = self.binaryTreePaths(root)
        res = []
        for i in all_path:
            if sum(i) == expectNumber:
                res.append(i)
        return res

    def binaryTreePaths(self, root):
        res = []
        self.findAllPath(root, [], res)
        return res
    
    def findAllPath(self, root, arr, res):
        if not root:
            return

        arr.append(root.val)
        if not root.left and not root.right:
            res.append(arr)
            return

        if root.left:
            self.findAllPath(root.left, arr[:], res)
        if root.right:
            self.findAllPath(root.right, arr[:], res)

node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)
node_8 = TreeNode(8)
node_9 = TreeNode(9)
node_10 = TreeNode(10)
node_11 = TreeNode(11)

node_8.left = node_6
node_8.right = node_10
node_6.left = node_5
node_6.right = node_7
node_10.left = node_9
node_10.right = node_11

res = Solution().FindPath(node_8, 29)
print(res)