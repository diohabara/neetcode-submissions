class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        res = 0
        for right, c in enumerate(s):
            if 0 < count[c]:
                while s[left] != c:
                    count[s[left]] -= 1
                    left += 1
                count[s[left]] -= 1
                left += 1
            count[c] += 1
            res = max(res, right-left+1)
        return res