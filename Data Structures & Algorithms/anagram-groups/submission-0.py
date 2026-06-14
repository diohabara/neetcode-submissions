class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {hashed_soted_str => list of strings}
        res = defaultdict(list)
        for s in strs:
            k = tuple(sorted(s))
            res[k].append(s)
        return [v for v in res.values()]