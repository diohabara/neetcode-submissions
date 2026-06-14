from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set, t_set = defaultdict(int), defaultdict(int)
        for c in s:
            s_set[c] += 1
        for c in t:
            t_set[c] += 1
        return s_set == t_set