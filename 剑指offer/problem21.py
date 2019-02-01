# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

class Solution:
    stack = []
    min_stack = []
    def push(self, node):
        self.stack.append(node)
        if len(self.min_stack) == 0 or node < self.min():
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min())

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
