class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur_index = 0
        min_index = min([len(s) for s in strs])
        while cur_index < min_index and all(s[cur_index] == strs[0][cur_index] for s in strs):
            cur_index += 1
        return strs[0][:cur_index]