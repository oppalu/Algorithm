# 请实现两个函数，分别用来序列化和反序列化二叉树
# 序列化：前序遍历，空节点用#代替。用，分隔开
# 反序列化：创建二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.index = -1

    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        self.index += 1
        data = s.split(',')
        node = None
        if self.index >= len(data):
            return node

        if data[self.index] != '#':
            node = TreeNode(int(data[self.index]))
            node.left = self.Deserialize(s)
            node.right = self.Deserialize(s)

        return node


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

# res = Solution().Serialize(node_8)
# print(res)

s = '8,6,5,#,#,7,#,#,10,9,#,#,11,#,#'
s2 = '5,4,#,3,#,2'
root = Solution().Deserialize(s2)

print(root.left.val)
print(root.right.val)