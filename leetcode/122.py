# best time to buy and sell stock 2

# you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
# 思路：
# the profit of the transaction
# = Prices[Y] - Prices[X] 
# = Prices[Y] - Prices[Y-1] +
#    Prices[Y-1] - Prices[Y-2] ...
#     ....
#    Prices[X+1] - Prices[X] 
# = D[Y] + D[Y-1] + ... + D[X+1]
# = sum of D from X+1 to Y

class Solution:
    # 40 ms, faster than 99.37%
    def maxProfit(self, prices: 'List[int]') -> 'int':
        res = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                res += (prices[i+1]-prices[i])
        return res
