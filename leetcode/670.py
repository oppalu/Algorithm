# maximum swap
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. 
# Return the maximum valued number you could get.
# ex:
# Input: 2736
# Output: 7236

class Solution:
    # 32 ms, faster than 100.00%
    def maximumSwap(self, num: 'int') -> 'int':
        data = [int(i) for i in str(num)]
        temp = sorted(data)
        temp.reverse()

        for i in range(len(data)):
            if data[i] != temp[i]:
                for j in range(len(data)-1, i, -1):
                    if data[j] == temp[i]:
                        data[i], data[j] = data[j], data[i]
                        return int(''.join(str(i) for i in data))

        return num
print(Solution().maximumSwap(1993))