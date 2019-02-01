# valid anagram
# Given two strings s and t , write a function to determine if t is an anagram[顺序调整后的] of s.
# ex：s = "anagram", t = "nagaram"【T】
# s = "rat", t = "car"【F】

class Solution(object):
    def isAnagram(self, s, t):
        # 88 ms, faster than 12.68% 
        if not s and not t:
            return True
        if not s or not t:
            return False
        s_arr = sorted(list(s))
        t_arr = sorted(list(t))
        return s_arr == t_arr

    def isAnagram2(self, s, t):
        # 56 ms, faster than 69.82%
        maps = {}
        mapt = {}
        for c in s:
            maps[c] = maps.get(c,0)+1
        for c in t:
            mapt[c] = mapt.get(c,0)+1
        return maps == mapt
    

print(Solution().isAnagram('anagram', ''))

