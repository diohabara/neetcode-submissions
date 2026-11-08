class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        required = len(need)

        window = {}
        have = 0

        min_len = float("inf")
        best = (0, 0)

        l = 0
        for r, c in enumerate(s):
            # 右端の文字を追加
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1

            # 条件を満たしている間、左端を縮める
            while have == required:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    best = (l, r)

                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1

        if min_len == float("inf"):
            return ""

        l, r = best
        return s[l : r + 1]