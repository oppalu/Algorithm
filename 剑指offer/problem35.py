# 第一个只出现一次的字符
# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回-1（需要区分大小写）

from collections import Counter
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1

    


print(Solution().FirstNotRepeatingChar("abaccdeff"))
print(Solution().FirstNotRepeatingChar(""))