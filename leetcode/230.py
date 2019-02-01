# kth smallest element in a BST
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        # 80 ms, faster than 18.42% 
        if not root:
            return root  
        if k <= 0:
            return None

        def iter_tree(pRoot):
            if not pRoot:
                return
            node.append([pRoot, pRoot.val])
            iter_tree(pRoot.left)
            iter_tree(pRoot.right)

        node = []
        iter_tree(root)
        node = sorted(node, key=lambda x: (x[1], x[0]))

        return node[k-1][0].val if k<=len(node) else None

    def kthSmallest2(self, root, k):
        # 由于是二叉搜索树，所以根节点比左子树的大，比右子树的小。
        # 先把左边的均进栈，如果当前是最小的就返回，否则遍历当前的右节点进栈(右节点还是比当前的父节点值小)
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            print(stack)
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

node_5 = TreeNode(5)
node_3 = TreeNode(3)
node_6 = TreeNode(6)
node_2 = TreeNode(2)
node_4 = TreeNode(4)
node_1 = TreeNode(1)

node_5.left = node_3
node_5.right = node_6
node_3.left = node_2
node_3.right = node_4
node_2.left = node_1
print(Solution().kthSmallest2(node_5, 3))