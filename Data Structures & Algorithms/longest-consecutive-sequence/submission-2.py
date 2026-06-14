class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        print(nums)
        res = 1
        cur = nums[0]
        streak = 1
        for n in nums[1:]:
            if cur + 1 == n:
                streak += 1
            else:
                streak = 1
            cur = n
            res = max(res, streak)
        return res