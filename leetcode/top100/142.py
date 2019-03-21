# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 40 ms, 100.00%
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                new_fast = head
                while new_fast != slow:
                    slow = slow.next
                    new_fast = new_fast.next
                return slow

        return None
        