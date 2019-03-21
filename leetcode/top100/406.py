# queue reconstruction by height

# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
# where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h.
# Write an algorithm to reconstruct the queue.

# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# [[8,2],[4,2],[4,5],[2,0],[7,2],[1,4],[9,1],[3,1],[9,0],[1,0]]
# [[1,0],[2,0],[9,0],[3,1],[1,4],[9,1],[4,2],[7,2],[8,2],[4,5]]

class Solution:        
    def reconstructQueue(self, people):
        # 从最高的开始排，然后按顺序，插入到x[1]对应的位置
        # 84 ms, 74.30%
        if not people or len(people) <= 1:
            return people

        people.sort()
        people.reverse()
        
        height = []
        temp = []
        max_v = people[0][0]
        for i in people:
            if i[0] == max_v:
                temp.append(i)
            else:
                temp.sort()
                height += temp
                temp = [i]
                max_v = i[0]
        temp.sort()
        height += temp

        res = []
        for i in height:
            res.insert(i[1], i)
        
        return res

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
people2 = [[8,2],[4,2],[4,5],[2,0],[7,2],[1,4],[9,1],[3,1],[9,0],[1,0]]
print(Solution().reconstructQueue(people2))