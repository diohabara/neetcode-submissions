class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        freq_until_j = defaultdict(int) # freq of total(0-j)
        freq_until_j[0] = 1
        res = 0
        for n in nums:
            # j < i
            # 0-i = current_sum
            # 0-j = current_sum - k
            # j-i = k
            current_sum += n
            residual = current_sum - k
            res += freq_until_j[residual]
            freq_until_j[current_sum] += 1
        return res