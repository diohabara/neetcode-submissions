class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                prev = i-c
                if prev<0:
                    continue
                dp[i] = min(dp[i], dp[prev]+1)
        return dp[-1] if dp[-1] != float('inf') else -1