# 删除链表中重复的结点
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        # 用一个new_head是为了防止开头就是重复的情况，如1-1-1-1-2
        new_head = ListNode(-1)
        new_head.next = pHead
        pre = new_head
        cur = pHead
        cur_next = None

        while cur and cur.next:
            cur_next = cur.next
            if cur.val == cur_next.val:
                while cur_next and cur_next.val == cur.val:
                    cur_next = cur_next.next
                pre.next = cur_next
                cur = cur_next
            else:
                pre = cur
                cur = cur.next
        return new_head.next

arr = [1,1,1,1,2]
head = ListNode(-1)
cur = head
for i in arr:
    cur.next = ListNode(i)
    cur = cur.next

new_head = Solution().deleteDuplication(head.next)
while new_head:
    print(new_head.val)
    new_head = new_head.next