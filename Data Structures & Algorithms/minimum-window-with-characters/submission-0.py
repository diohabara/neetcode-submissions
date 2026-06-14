class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t) # need[c]: cがいくつ必要か 
        missing = len(t) # tの不足している文字数
        l = 0
        best_l = 0
        best_size = len(s) + 1
        for r, c in enumerate(s):
            if 0 < need[c]:
                missing -= 1
            need[c] -= 1
            while missing == 0:
                cur_l = r - l + 1
                if cur_l < best_size:
                    best_size = cur_l
                    best_l = l
                drop = s[l]
                need[drop] += 1
                if 0 < need[drop]:
                    missing += 1
                l += 1
        if best_size <= len(s):
            return s[best_l :best_l + best_size]
        return ""