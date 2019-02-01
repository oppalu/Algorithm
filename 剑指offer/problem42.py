# 翻转单词顺序列
# ex: I am a student. -> student. a am I

class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        words = s.split()
        if len(words) == 0:
            return s
        else:
            s2=[]
            for i in words:
                s2.append(i)
                s2.append(' ')
            s2.reverse()
            return ''.join(s2).strip()


print(Solution().ReverseSentence("I am a student."))