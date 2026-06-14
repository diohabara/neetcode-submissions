class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        counter = Counter(nums)
        res = []
        for n, count in counter.items():
            if threshold < count:
                res.append(n)
        return res