class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # char -> recent index
        left = 0
        res = 0
        for right, c in enumerate(s):
            if c in char_map and left <= char_map[c]:
                left = char_map[c] + 1
            char_map[c] = right
            res = max(res, right-left+1)
        return res