# 表示数值的字符串:请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
# e只能出现一次后面必须带一个整数(可带符号)，小数点只能出现一次，不能出现非e的其他字母。+-号不能连在一起

import re
class Solution:
    def isNumeric(self, s):
        hasE = False
        hasPoint = False
        hasSymbol = False

        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                if hasE or i == len(s)-1:
                    return False
                hasE = True
            elif s[i] == '.':
                if hasPoint or hasE:
                    return False
                hasPoint = True
            elif s[i] == '+' or s[i] == '-':
                # 已经出现符号，则只能出现在e后面
                if hasSymbol and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                # 没有出现符号，但不在开头也必须出现在e后面
                if not hasSymbol and i != 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False 
                hasSymbol = True
            elif s[i] < '0' or s[i] > '9':
                return False
        return True

    def isNumeric2(self, s):
        # 法二，正则表达式
        res = re.match("^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$",s)
        return False if not res else True


print(Solution().isNumeric('123.45e+6'))
print(Solution().isNumeric2('123.45e+6'))