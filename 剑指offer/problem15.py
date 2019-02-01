# 输入一个链表，输出该链表中倒数第k个结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return None

        iter_fast = head
        for _ in range(k):
            if iter_fast.next:
                iter_fast = iter_fast.next
            else:
                return None
            
        while iter_fast:
            head = head.next
            iter_fast = iter_fast.next

        return head

    def FindKthToTail2(self, head, k):
        # write code here
        front = head
        later = head
        for i in range(k):
            if front==None:
                return
            if front.next == None and i==k-1:
                return head
            front = front.next
        while front.next != None:
            front = front.next
            later = later.next
        return later.next


arr = [1,2,3,4,5,6,7,8]
head = ListNode(-1)
cur = head
for i in arr:
    node = ListNode(i)
    cur.next = node
    cur = node

res = Solution().FindKthToTail(head.next,5)
print(res.val)