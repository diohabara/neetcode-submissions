class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26
        l = 0
        max_freq = 0
        ans = 0

        for r, ch in enumerate(s):
            idx = ord(ch) - ord('A')
            cnt[idx] += 1
            max_freq = max(max_freq, cnt[idx])

            # この区間を同一文字に揃えるのに必要な置換が k を超えたら左を縮める
            while (r - l + 1) - max_freq > k:
                left_idx = ord(s[l]) - ord('A')
                cnt[left_idx] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
