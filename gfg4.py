class Solution:
    def maximumProfit(self, prices):
        minp = float('inf')
        maxp = 0
        for price in prices:
            if price < minp:
                minp = price
            elif price - minp > maxp:
                maxp = price - minp
        return maxp        