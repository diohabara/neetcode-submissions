class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        cur_p = 0
        cheapest = float('inf')
        for p in prices:
            if cheapest < p:
                cur_p = p - cheapest
            cheapest = min(cheapest, p)
            max_p = max(max_p, cur_p)
        return max_p