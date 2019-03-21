# word subsets
# We are given two arrays A and B of words.  Each word is a string of lowercase letters.
# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".
# Now say a word a from A is universal if for every b in B, b is a subset of a. 
# Return a list of all universal words in A.  You can return the words in any order.

from collections import Counter
class Solution:
    def wordSubsets(self, A, B) -> 'List[str]':
        # 2008 ms, 5.22%; 16.2 MB,20.00% 
        b_dict = {}
        for b in B:
            count = Counter(b)
            for k,v in count.items():
                if k not in b_dict or b_dict[k] < v:
                    b_dict[k] = v

        res = A.copy()

        for a in A:
            count = Counter(a)
            for k,v in b_dict.items():
                if k not in count or count[k] < v:
                    res.remove(a)
                    break

        return res

        # res = A.copy()
        # for a in A:
        #     for b in B:
        #         if not self.subset(a,b):
        #             res.remove(a)
        #             break
        # return res

A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","oo"]
print(Solution().wordSubsets(A, B))

