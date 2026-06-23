class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""
        need = Counter(t)
        window = defaultdict(int)
        have = 0
        required = len(need)
        best_len = float('inf')
        best_l = 0
        l = 0
        for r, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                have += 1
            while have == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                left_ch = s[l]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                l += 1
        return "" if best_len == float('inf') else s[best_l: best_l+best_len]
