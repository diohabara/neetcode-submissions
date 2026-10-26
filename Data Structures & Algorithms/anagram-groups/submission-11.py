class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def s2c(s: str) -> tuple[int]:
            counts = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                counts[idx] += 1
            return tuple(counts)
        count2strs = defaultdict(list)
        for s in strs:
            count = s2c(s)
            count2strs[count].append(s)
        return [l for l in count2strs.values()]