# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
# 思路：把新的点放在原点的后面，然后新的random就是原来random的next

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        cur = pHead
        while cur:
            temp = RandomListNode(cur.label)
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        
        cur = pHead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        new_head = pHead.next
        cur = new_head
        pHead = pHead.next
        while pHead.next:
            pHead = pHead.next.next
            cur.next = pHead
            cur = cur.next
            
        return new_head

node_a = RandomListNode('a')
node_b = RandomListNode('b')
node_c = RandomListNode('c')
node_d = RandomListNode('d')
node_e = RandomListNode('e')

node_a.next = node_b
node_a.random = node_c
node_b.next = node_c
node_b.random = node_e
node_c.next = node_d
node_d.next = node_e
node_d.random = node_b

new_head = Solution().Clone(node_a)
