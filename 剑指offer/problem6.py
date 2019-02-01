# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre is None or len(pre) == 0:
            return
        
        root_val = pre[0]
        root = TreeNode(root_val)

        i = 0
        while tin[i] != root_val:
            i += 1
        
        left_pre = pre[1:i+1]
        right_pre = pre[i+1:]
        left_tin = tin[0:i]
        right_tin = tin[i+1:]

        root.left = self.reConstructBinaryTree(left_pre, left_tin)
        root.right = self.reConstructBinaryTree(right_pre, right_tin)

        return root

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]

root = Solution().reConstructBinaryTree(pre, tin)