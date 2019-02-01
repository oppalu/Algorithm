# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def TreeDepth(pRoot):
            if not pRoot:
                return 0
            leftDepth = TreeDepth(pRoot.left)
            rightDepth = TreeDepth(pRoot.right)
            return 1+ max(leftDepth, rightDepth)

        if not pRoot:
            return True
        
        leftDepth = TreeDepth(pRoot.left)
        rightDepth = TreeDepth(pRoot.right)
        if abs(leftDepth-rightDepth) > 1:
            return False

        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        

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

print(Solution().TreeDepth(node_8))
