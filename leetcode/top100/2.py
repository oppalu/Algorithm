# Add two numbers

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        # 108ms, 67.59%
        plus = 0
        head = ListNode(-1)
        res = head
        while l1 or l2 or plus:
            op1 = op2 = 0
            if l1:
                op1 = l1.val
                l1 = l1.next
            if l2:
                op2 = l2.val
                l2 = l2.next
            plus, ans = divmod(op1+op2+plus, 10)
            res.next = ListNode(ans)
            res = res.next
        return head.next

node_2 = ListNode(2)
node_4 = ListNode(4)
node_3 = ListNode(3)

node_5 = ListNode(5)
node_6 = ListNode(6)
node_42 = ListNode(4)

node_2.next = node_4
node_4.next = node_3
node_5.next = node_6
node_6.next = node_42

res = Solution().addTwoNumbers(node_2, node_5)

while res:
    print(res.val)
    res = res.next