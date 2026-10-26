from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        for num, count in sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]:
            res.append(num)
        return res