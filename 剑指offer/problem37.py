# 输入两个链表，找出他们的第一个公共节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        
        arr1 = []
        arr2 = []
        while pHead1:
            arr1.append(pHead1)
            pHead1 = pHead1.next

        while pHead2:
            arr2.append(pHead2)
            pHead2 = pHead2.next

        res = None
        while len(arr1)>0 and len(arr2)>0 and arr1[-1] is arr2[-1]:
            res = arr1.pop()
            arr2.pop()

        return res
    

arr1 = [1,2,3,6,7]
arr2 = [6,7]

head1 = ListNode(-1)
head2 = ListNode(-1)
cur1 = head1
cur2 = head2
for i in arr1:
    node = ListNode(i)
    cur1.next = node
    cur1 = cur1.next

for i in arr2:
    node = ListNode(i)
    cur2.next = node
    cur2 = cur2.next

print(Solution().FindFirstCommonNode(head1.next, head2.next))