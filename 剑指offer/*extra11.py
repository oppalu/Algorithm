# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        res = []
        if pRoot == None:
            return res
        queue = []
        queue.append(pRoot)

        while len(queue) > 0:
            layer = []
            num = len(queue)
            while num>0:
                cur = queue[0]
                layer.append(cur.val)
                queue = queue[1:]

                if cur.left != None:
                    queue.append(cur.left)
                
                if cur.right != None:
                    queue.append(cur.right)
                num -= 1
            res.append(layer)
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

res = Solution().Print(node_8)

print(res)