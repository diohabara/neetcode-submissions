class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_cnt = Counter(s1)
        m, n = len(s1), len(s2)
        # sliding windows, s1_cnt
        s2_cnt = Counter(s2[:m])
        for i in range(m, n):
            if s1_cnt == s2_cnt:
                return True
            s2_cnt[s2[i-m]] -= 1
            s2_cnt[s2[i]] += 1
        return s1_cnt == s2_cnt