class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        for sc, tc in zip(sorted(s), sorted(t)):
            if sc != tc:
                return False
        return True