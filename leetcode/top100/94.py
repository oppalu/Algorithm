# Given a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

    def inorderTraversal(self, root):
        # 36 ms, 75.31%
        self.res = []

        self.inorder(root)

        return self.res