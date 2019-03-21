# Minimum Cost For Tickets
# In a country popular for train travel, you have planned some train travelling one year in advance.  
# The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.
# Train tickets are sold in 3 different ways:
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# Return the minimum number of dollars you need to travel every day in the given list of days.

class Solution:
    def mincostTickets(self, days, costs):
        res = [0 for i in range(days[-1]+1)]
        
        for i in range(days[-1]+1):
            if i not in days:
                res[i] = res[i-1]
            else:
                res[i] = min(res[max(0,i-1)]+costs[0], res[max(0,i-7)]+costs[1], res[max(0,i-30)]+costs[2])

        print(res)
        return res[-1]

# days = [1,4,6,7,8,20]
# costs = [2,7,15]
# print(Solution().mincostTickets(days, costs))

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(Solution().mincostTickets(days, costs))