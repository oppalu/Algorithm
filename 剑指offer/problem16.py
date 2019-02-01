# 输入一个链表，反转链表后，输出新链表的表头。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        new_head = None

        if pHead is None:
            return new_head

        pre = None
        cur = pHead

        while cur:
            pNext = cur.next
            if pNext is None:
                new_head = cur
            cur.next = pre
            pre = cur
            cur = pNext

        return new_head

arr = [1,2,3,4,5,6,7,8]
head = ListNode(-1)
cur = head
for i in arr:
    node = ListNode(i)
    cur.next = node
    cur = node

res = Solution().ReverseList(head.next)

while res:
    print(res.val)
    res = res.next

