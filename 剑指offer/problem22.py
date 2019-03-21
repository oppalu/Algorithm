# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。

class Solution:
    def IsPopOrder2(self, pushV, popV):
        stack = []
        i = j = 0
        while i < len(pushV):
            if pushV[i] == popV[j]:
                i += 1
                j += 1
            elif stack and stack[-1] == popV[j]:
                stack.pop()
                j += 1
            else:
                stack.append(pushV[i])
                i += 1

        while stack:
            data = stack.pop()
            if data != popV[j]:
                return False
            j += 1
        return True


    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []

        i = j = 0
        while i != len(pushV):
            if pushV[i] == popV[j]:
                i += 1
                j += 1
            else:
                if len(stack) == 0 or popV[j] != stack[-1]:
                    stack.append(pushV[i])
                    i += 1
                else:
                    j += 1
                    stack.pop()

        while j != len(pushV):
            if popV[j] == stack[-1]:
                stack.pop()
            j += 1
        
        return len(stack) == 0

push = [1,2,3,4,5]
pop = [4,5,3,2,1]

print(Solution().IsPopOrder2(push, pop))