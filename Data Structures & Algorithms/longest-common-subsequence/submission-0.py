class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # dp[i][j] = text1[0:i] と text2[0:j] の LCS の長さ
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 今見ている prefix の最後の文字が同じなら、
                # その文字を LCS に追加できる
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                # 最後の文字が違うなら、
                # text1 側を1文字捨てるか、text2 側を1文字捨てる
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]