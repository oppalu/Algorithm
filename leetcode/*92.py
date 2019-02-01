# reverse linked list2
#  Reverse a linked list from position m to n. Do it in one-pass.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
class Solution(object):
    def reverseBetween(self, head, m, n):
        # 20ms,100%
        new_head = ListNode(-1)
        new_head.next = head
        pre = new_head
        
        for _ in range(m-1):
            pre = pre.next
        
        cur = pre.next
        post = cur.next

        for _ in range(n-m):
            cur.next = post.next
            post.next = pre.next
            pre.next = post
            post = cur.next
        return new_head.next

arr = [1,2]
head = ListNode(-1)
cur = head
for i in arr:
    node = ListNode(i)
    cur.next = node
    cur = node

res = Solution().reverseBetween(head.next,1,2)

while res:
    print(res.val)
    res = res.next