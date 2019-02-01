# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return pRoot  
        if k <= 0:
            return None

        def iter_tree(pRoot):
            if not pRoot:
                return
            node.append([pRoot, pRoot.val])
            iter_tree(pRoot.left)
            iter_tree(pRoot.right)

        node = []
        iter_tree(pRoot)
        node = sorted(node, key=lambda x: (x[1], x[0]))
        return node[k-1][0] if k<=len(node) else None
    
    def KthNode2(self, pRoot, k):
        # 方法2，中序遍历即是排好序的
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            node.append(root.val)
            inorder(root.right)

        node = []
        if not pRoot:
            return pRoot  
        if k <= 0:
            return None
        inorder(pRoot)
        return node[k-1] if k<=len(node) else None


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

res = Solution().KthNode2(node_8, 3)
print(res)
