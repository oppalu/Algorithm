# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None

        if not pNode.right:
            # 右子树为空，如果当前是左子树则返回父节点，否则返回最父节点
            while pNode.next:
                if pNode.next.left is pNode:
                    return pNode.next
                pNode = pNode.next
        else:
            # 右子树不为空返回右子树的最左节点
            temp = pNode.right
            while temp.left:
                temp = temp.left
            return temp

node_5 = TreeLinkNode(5)
node_6 = TreeLinkNode(6)
node_7 = TreeLinkNode(7)
node_8 = TreeLinkNode(8)
node_9 = TreeLinkNode(9)
node_10 = TreeLinkNode(10)
node_11 = TreeLinkNode(11)

node_8.left = node_6
node_8.right = node_10
node_6.left = node_5
node_6.right = node_7
node_10.left = node_9
node_10.right = node_11

node_5.next = node_6
node_7.next = node_6
node_6.next = node_8
node_9.next = node_10
node_11.next = node_10
node_10.next = node_8

node = Solution().GetNext(node_11)

print(node.val)