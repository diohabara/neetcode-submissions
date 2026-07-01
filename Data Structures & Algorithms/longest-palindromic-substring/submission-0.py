class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        best_start = 0
        best_len = 1
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and length > best_len:
                    best_start = i
                    best_len = length
        return s[best_start:best_start+best_len]