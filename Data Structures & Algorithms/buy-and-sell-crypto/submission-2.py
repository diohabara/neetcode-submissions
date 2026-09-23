class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = prices[0]
        for p in prices:
            new_profit = p - min_p
            profit = max(profit, new_profit)
            min_p = min(min_p, p)
        return profit