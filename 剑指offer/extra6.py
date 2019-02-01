# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None

        data = []
        while pHead:
            if pHead in data:
                return pHead
            data.append(pHead)
            pHead = pHead.next
        return None

    def EntryNodeOfLoop2(self, pHead):
        slow,fast=pHead,pHead
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow2=pHead
                while slow!=slow2:
                    slow=slow.next
                    slow2=slow2.next
                return slow