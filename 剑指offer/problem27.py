# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
# （中序输出）

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here

        def inorder(root):
            if not root:
                return
            if root.left:
                inorder(root.left)

            res.append(TreeNode(root.val))

            if root.right:
                inorder(root.right)

        if not pRootOfTree:
            return None
        res = []
        inorder(pRootOfTree)

        for i in range(len(res)):
            if i > 0:
                res[i].left = res[i-1]
            if i < len(res)-1:
                res[i].right = res[i+1]
        return res[0]

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

res = Solution().Convert(None)