class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l, maxf, res = 0, 0, 0
        for r, c in enumerate(s):
            freq[c] += 1
            maxf = max(maxf, freq[c])
            while k < (r-l+1) - maxf:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res