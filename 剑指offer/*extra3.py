# 正则表达式的匹配:请实现一个函数用来匹配包括'.'和'*'的正则表达式。
# 模式中的字符'.'表示匹配任意一个字符，而'*'表示零次或多次匹配前面的字符或子表达式(如runoo*b也可以匹配runob)
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

# 首先，考虑特殊情况：
    # 1>两个字符串都为空，返回true
    # 2>当第一个字符串不空，而第二个字符串空了，返回false（因为这样，就无法匹配成功了,而如果第一个字符串空了，第二个字符串非空，
    # 还是可能匹配成功的，比如第二个字符串是“a*a*a*a*”,由于‘*’之前的元素可以出现0次， 所以有可能匹配成功）
# 之后就开始匹配第一个字符:考虑到pattern下一个字符可能是‘*’， 这里我们分两种情况讨论：pattern下一个字符为‘*’或不为‘*’
    # 1>pattern下一个字符不为‘*’：这种情况比较简单，直接匹配当前字符。如果匹配成功，继续匹配下一个；如果匹配失败，直接返回false。
    # 2>pattern下一个字符为‘*’时：
        # a>当‘*’匹配0个字符时，str当前字符不变，pattern当前字符后移两位，跳过这个‘*’符号
        # b>当‘*’匹配1个或多个时，str当前字符移向下一个，pattern当前字符不变。
        # （这里匹配1个或多个可以看成一种情况，因为：当匹配一个时，由于str移到了下一个字符，而pattern字符不变，就回到了上边的情况a；
        # 当匹配多于一个字符时，相当于从str的下一个字符继续开始匹配）

class Solution:
        
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        
        if len(pattern) > 1 and pattern[1] == '*':
            if (len(s)==0) or (s[0] != pattern[0] and pattern[0] != '.'):
                # 匹配0个的情况
                return self.match(s, pattern[2:])
            else:
                # 匹配1次 or 匹配多次 or 匹配0次(防止a与a*a的情况)
                return self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern) or self.match(s, pattern[2:])            
        else:
            if len(s) == 0:
                return False
            if s[0] == pattern[0] or pattern[0] == '.':
                return self.match(s[1:], pattern[1:])
            else:
                return False

print(Solution().match("a","a*a"))

print(Solution().match("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))

