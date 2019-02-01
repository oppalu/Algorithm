# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2

        if pHead2 is None:
            return pHead1
        
        head = ListNode(-1)
        cur1 = pHead1
        cur2 = pHead2

        cur = head
        while True:
            if cur1.val < cur2.val:
                cur.next = ListNode(cur1.val)
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = ListNode(cur2.val)
                cur = cur.next
                cur2 = cur2.next

            if cur1 is None and cur2:
                cur.next = cur2
                break

            if cur2 is None and cur1:
                cur.next = cur1
                break
    
        return head.next

    
    def Merge2(self, pHead1, pHead2):
        # 使用递归
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        
        head = None
        if pHead1.val < pHead2.val:
            head = ListNode(pHead1.val)
            head.next = self.Merge2(pHead1.next, pHead2)
        else:
            head = ListNode(pHead2.val)
            head.next = self.Merge2(pHead1, pHead2.next)
    
        return head

arr1 = [1,3,5,7]
arr2 = [1,2,4,6,8]

head1 = ListNode(-1)
cur1 = head1
for i in arr1:
    node = ListNode(i)
    cur1.next = node
    cur1 = node


head2 = ListNode(-1)
cur2 = head2
for i in arr2:
    node = ListNode(i)
    cur2.next = node
    cur2 = node

res = Solution().Merge2(head1.next, head2.next)

while res:
    print(res.val)
    res = res.next