class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur = 0
        n = len(nums)
        res = n+1
        for r in range(n):
            cur += nums[r]
            while target <= cur - nums[l]:
                cur -= nums[l]
                l += 1
            if target <= cur:
                res = min(res, r-l+1)
        if res == n+1:
            return 0
        else:
            return res