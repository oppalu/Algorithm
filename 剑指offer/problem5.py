# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList（不允许改变链表结构）

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        if listNode is None:
            return res

        arr = []
        while listNode:
            arr.append(listNode.val)
            listNode = listNode.next

        while len(arr) > 0:
            res.append(arr.pop())

        return res



l = [1,2,3]
head = ListNode(-1)
cur = head
for i in l:
    node = ListNode(i)
    cur.next = node
    cur = cur.next

head = head.next
res = Solution().printListFromTailToHead(head)
print(res)



