# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        queue = []

        if root == None:
            return res

        queue.append(root)

        while len(queue) > 0:
            cur = queue[0]
            res.append(cur.val)
            queue = queue[1:]

            if cur.left != None:
                queue.append(cur.left)
            
            if cur.right != None:
                queue.append(cur.right)

        return res

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

res = Solution().PrintFromTopToBottom(node_8)

print(res)