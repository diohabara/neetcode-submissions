class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        words = defaultdict(int)
        l, r, n = 0, 0, len(s)
        res = 0
        while r < n:
            words[s[r]] += 1
            while 1 < words[s[r]]:
                words[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
