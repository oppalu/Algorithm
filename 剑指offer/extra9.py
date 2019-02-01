# 对称的二叉树：请实现一个函数，用来判断一颗二叉树是不是对称的。（判断左右子树是否相同）

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    def equals(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False
        
        return self.equals(root1.left, root2.right) and self.equals(root2.left, root1.right)

    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.equals(pRoot.left, pRoot.right)


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
node_11.left = TreeNode(1)
node_11.right = TreeNode(1)
print(Solution().isSymmetrical(node_11))

