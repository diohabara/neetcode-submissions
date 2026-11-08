class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        n = len(s1)
        left = 0
        for right, c in enumerate(s2):
            counter[c] -= 1
            while counter[c] < 0:
                counter[s2[left]] += 1
                left += 1
            else:
                if right - left + 1 == n:
                    return True
        return False