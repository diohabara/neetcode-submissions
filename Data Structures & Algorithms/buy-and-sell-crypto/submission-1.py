class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest = float('inf')
        for p in prices:
            cheapest = min(cheapest, p)
            profit = max(profit, p - cheapest)
        return profit