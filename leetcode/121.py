# Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction, design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

class Solution:
    # 4520 ms, faster than 1.54% 
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices or len(prices)==0:
            return 0

        res = 0
        for i in range(len(prices)-1):
            current = prices[i]
            temp_max = max(prices[i+1:])
            if temp_max > current:
                if (temp_max-current) > res:
                    res = temp_max-current
        return res

    # 44 ms, faster than 85.61% 
    def maxProfit2(self, prices: 'List[int]') -> 'int':
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

arr = [7,6,4,3,1]
print(Solution().maxProfit(arr))