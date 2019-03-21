# Given a binary tree, determine if it is a valid binary search tree (BST).

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, root):
        if not root:
            return
        if root.left:
            self.dfs(root.left)
        self.res.append(root.val)
        if root.right:
            self.dfs(root.right)

    def isValidBST(self, root):
        # 36 ms, 94.70% 
        self.res = []

        self.dfs(root)
        
        for i in range(len(self.res)-1):
            if self.res[i] >= self.res[i+1]:
                return False
        return True
        

node_3 = TreeNode(3)
node_9 = TreeNode(9)
node_20 = TreeNode(20)
node_15 = TreeNode(15)
node_7 = TreeNode(7)

node_3.left = node_9
node_3.right = node_20
node_20.left = node_15
node_20.right = node_7
Solution().isValidBST(node_3)