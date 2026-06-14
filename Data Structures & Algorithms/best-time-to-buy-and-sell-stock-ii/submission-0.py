class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        cur = float("inf")
        for p in prices:
            if cur < p:
                total += (p - cur)
            cur = p
        return total