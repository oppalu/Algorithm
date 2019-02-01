# BinaryTree path
# Given a binary tree, return all root-to-leaf paths.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        res = []
        self.findPath(root, [], res)
        result = []
        for data in res:
            result.append("->".join(str(i) for i in data))
        return result
    
    def findPath(self, root, arr, res):
        if not root:
            return

        arr.append(root.val)
        if not root.left and not root.right:
            res.append(arr)
            return

        if root.left:
            self.findPath(root.left, arr[:], res)
        if root.right:
            self.findPath(root.right, arr[:], res)

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

print(Solution().binaryTreePaths(node_8))