class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        n = len(s)
        used = set([s[0]])
        longest = 1
        cur = 1
        # slide (l, r)
        for r in range(1, n):
            while s[r] in used:
                used.remove(s[l])
                l += 1
            used.add(s[r])
            cur = r-l+1
            longest = max(longest, cur)
        return longest