class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[r][c] = (r, c) に到達する経路数
        dp = [[1] * n for _ in range(m)]

        # 一番上の行と一番左の列はすでに 1
        # それ以外のマスを埋める
        for r in range(1, m):
            for c in range(1, n):
                # 上から来る経路数 + 左から来る経路数
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]