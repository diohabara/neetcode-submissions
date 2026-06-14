class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for cnt in range(len(freq) - 1, 0, -1):
            res.extend(freq[cnt])
            if len(res) >= k:
                return res[:k]