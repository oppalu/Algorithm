# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，其他行以此类推。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        res = []
        if pRoot == None:
            return res
        queue = []
        queue.append(pRoot)
        is_reverse = False

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
            if is_reverse:
                layer.reverse()
            res.append(layer)
            is_reverse = not is_reverse
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