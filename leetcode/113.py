# Path sum
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def pathSum(self, root, sum):
        res = []
    
        def findPathSum(root, arr, currentValue):
            if not root:
                return
            arr.append(root.val)

            if not root.left and not root.right and currentValue == root.val:
                res.append(arr)
                return

            if root.left:
                findPathSum(root.left, arr[:], currentValue-root.val)
            if root.right:
                findPathSum(root.right, arr[:], currentValue-root.val)

        findPathSum(root, [], sum)
        return res

node_10 = TreeNode(10)
node_5 = TreeNode(5)
node_4 = TreeNode(4)
node_7 = TreeNode(7)
node_12 = TreeNode(12)

node_10.left = node_5
node_10.right = node_12
node_5.left = node_4
node_5.right = node_7

print(Solution().pathSum(node_10, 22))