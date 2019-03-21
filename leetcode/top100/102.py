# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 44 ms, 63.55%
    def levelOrder(self, root):
        res = []
        if not root:
            return res

        queue = []
        queue.append(root)

        while queue:
            layer = []
            num = len(queue)
            while num > 0:
                node = queue[0]
                layer.append(node.val)
                queue = queue[1:]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                num -= 1

            res.append(layer)
        return res


node_3 = TreeNode(3)
node_9 = TreeNode(9)
node_20 = TreeNode(20)
node_15 = TreeNode(15)
node_7 = TreeNode(7)

node_3.left = node_9
node_3.right = node_20
node_20.left = node_15
node_20.right = node_7

Solution().levelOrder(node_3)